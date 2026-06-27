"""基础评估 API — 出题 + 提交评分 + 人物画像 + 学习计划定制"""
import json
import os
from fastapi import APIRouter, Query
from pydantic import BaseModel
from typing import List, Optional
from services.assessor import get_assessment, grade_assessment
from services.achievement import record_assessment
from services.profile_service import profile_service
from rag.embedder import embedder
from rag.knowledge_base import knowledge_base
from rag.user_memory import user_memory
from data_utils import get_user_data_path, ensure_user_dir, migrate_global_data_if_needed

router = APIRouter(prefix="/api/assessment")

_last_results: dict[str, dict] = {}  # user_id → {language: result}
_last_question_ids: dict[str, list[str]] = {}  # user_id → question_ids
_last_profile: dict[str, dict] = {}  # user_id → profile
_last_plan: dict[str, dict] = {}  # user_id → plan

# 向后兼容：迁移旧格式（单层 → 按语言分层）
def _migrate_results_file(filepath: str):
    """将旧格式 {score,level,...} 迁移为 {lang: {score,level,...}}"""
    try:
        if not os.path.exists(filepath):
            return
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, dict) and "score" in data and "level" in data:
            # 旧格式：顶层是单条评估结果 → 包装进 "python"
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump({"python": data}, f, ensure_ascii=False, indent=2)
    except Exception:
        pass


def _load_from_file(user_id: str):
    """加载指定用户的数据到内存"""
    global _last_results, _last_profile
    user_id = user_id.strip() if user_id and user_id.strip() else "default"

    if user_id not in _last_results:
        _last_results[user_id] = {}
    if user_id not in _last_question_ids:
        _last_question_ids[user_id] = []

    result_path = get_user_data_path(user_id, "assessment_result.json")
    profile_path = get_user_data_path(user_id, "user_profile.json")

    migrate_global_data_if_needed(user_id)
    _migrate_results_file(result_path)

    try:
        if os.path.exists(result_path):
            with open(result_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            if isinstance(data, dict):
                _last_results[user_id] = data
    except Exception:
        pass
    try:
        if os.path.exists(profile_path):
            with open(profile_path, "r", encoding="utf-8") as f:
                _last_profile[user_id] = json.load(f)
    except Exception:
        pass


def _save_to_file(result: dict, language: str, user_id: str):
    user_id = user_id.strip() if user_id and user_id.strip() else "default"
    ensure_user_dir(user_id)
    migrate_global_data_if_needed(user_id)

    # 确保 user 级别的字典存在
    if user_id not in _last_results:
        _last_results[user_id] = {}
    if language:
        _last_results[user_id][language] = result

    filepath = get_user_data_path(user_id, "assessment_result.json")
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(_last_results[user_id], f, ensure_ascii=False, indent=2)


def _save_profile(profile: dict, user_id: str):
    user_id = user_id.strip() if user_id and user_id.strip() else "default"
    ensure_user_dir(user_id)
    migrate_global_data_if_needed(user_id)

    _last_profile[user_id] = profile
    filepath = get_user_data_path(user_id, "user_profile.json")
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(profile, f, ensure_ascii=False, indent=2)


class AssessmentRequest(BaseModel):
    language: str = "python"


class SubmitRequest(BaseModel):
    language: str = "python"
    answers: List[int] = []
    question_ids: List[str] = []


class ProfileRequest(BaseModel):
    experience: str = ""
    current_level: str = ""
    goals: str = ""
    time_per_week: str = ""
    learning_style: str = ""
    languages_known: List[str] = []
    target_language: str = "python"
    notes: str = ""


@router.post("/start")
async def start_assessment(req: AssessmentRequest, user_id: str = Query("default")):
    """获取评估题目（10 道选择题）"""
    global _last_question_ids
    _load_from_file(user_id)
    questions = get_assessment(req.language, count=10)
    _last_question_ids[user_id] = [q["id"] for q in questions]
    return {"language": req.language, "total": len(questions), "questions": questions}


@router.post("/submit")
async def submit_assessment(req: SubmitRequest, user_id: str = Query("default")):
    """提交答案，返回评分、等级和学习计划"""
    global _last_results, _last_question_ids
    qids = req.question_ids if req.question_ids else _last_question_ids.get(user_id, [])
    result = grade_assessment(req.language, req.answers, qids)
    result["language"] = req.language
    _save_to_file(result, req.language, user_id)
    score = result.get("score", 0)
    new_ach = record_assessment(int(score), req.language, user_id)
    result["new_achievements"] = new_ach
    return result


@router.get("/latest")
async def get_latest_assessment(language: str = "", user_id: str = Query("default")):
    """获取最近一次评估结果，可选语言过滤"""
    global _last_results
    _load_from_file(user_id)
    user_results = _last_results.get(user_id, {})
    if language:
        result = user_results.get(language)
        if result is None:
            return {"status": "not_taken", "language": language}
        return result
    # 未指定语言：返回最新的一条
    if not user_results:
        return {"status": "not_taken"}
    latest_lang = list(user_results.keys())[-1]
    return user_results[latest_lang]


@router.post("/profile")
async def create_profile(req: ProfileRequest, user_id: str = Query("default")):
    """
    生成人物画像：收集用户背景信息 -> LLM 生成结构化画像 ->
    embedding 向量化 -> 知识库语义检索 -> UserMemory 持久化
    """
    global _last_profile

    background = {
        "experience": req.experience,
        "current_level": req.current_level,
        "goals": req.goals,
        "time_per_week": req.time_per_week,
        "learning_style": req.learning_style,
        "languages_known": req.languages_known,
        "target_language": req.target_language,
        "notes": req.notes,
    }

    # Step 1: LLM 生成结构化人物画像
    profile = await profile_service.generate_profile(background)
    _last_profile[user_id] = profile
    _save_profile(profile, user_id)

    # Step 2: 画像向量化 + 知识库语义检索
    profile_text = json.dumps(profile, ensure_ascii=False)
    knowledge_matches = []
    try:
        # 构建搜索查询：组合标签 + 目标 + 薄弱点
        search_query_parts = []
        if profile.get("tags"):
            search_query_parts.append(" ".join(profile["tags"]))
        if profile.get("goals"):
            search_query_parts.append(" ".join(profile["goals"]))
        if profile.get("weaknesses"):
            search_query_parts.append(" ".join(profile["weaknesses"]))
        search_query = " ".join(search_query_parts) if search_query_parts else profile.get("summary", "")

        if search_query:
            knowledge_matches = knowledge_base.search(search_query, k=10)
    except Exception as e:
        print(f"[Profile] 知识库检索失败: {e}")

    # Step 3: UserMemory 持久化
    try:
        user_memory.remember(
            user_id=user_id,
            content=profile_text,
            memory_type="profile",
            metadata={
                "level": profile.get("level", ""),
                "tags": ",".join(profile.get("tags", [])),
                "target_language": req.target_language,
            }
        )
        # 同时把薄弱点写入
        for weakness in profile.get("weaknesses", []):
            user_memory.remember(
                user_id=user_id,
                content=weakness,
                memory_type="weakness",
                metadata={"source": "profile", "language": req.target_language}
            )
    except Exception as e:
        print(f"[Profile] UserMemory 写入失败: {e}")

    return {
        "profile": profile,
        "knowledge_matches": knowledge_matches,
        "knowledge_count": len(knowledge_matches),
    }


@router.get("/plan")
async def get_custom_plan(language: str = "", user_id: str = Query("default")):
    """
    获取定制学习计划：结合人物画像 + 答题评估结果 + 知识库语义检索结果 ->
    LLM 生成个性化学习计划。支持语言参数过滤。
    """
    global _last_profile, _last_results, _last_plan

    user_profile = _last_profile.get(user_id)
    if user_profile is None:
        return {
            "status": "no_profile",
            "message": "请先完成人物画像（POST /api/assessment/profile）和答题评估",
            "plan": None,
        }

    user_results = _last_results.get(user_id, {})
    # 按语言取评估结果
    lang_result = user_results.get(language) if language else None

    if user_results and language and lang_result is None:
        return {
            "status": "not_assessed",
            "message": f"尚未完成 {language} 语言的评估，请先评估",
            "plan": None,
        }

    if lang_result is None:
        # 仅有画像，生成不依赖答题结果的基础计划
        assessment_summary = {
            "score": None,
            "level": user_profile.get("level", "未知"),
            "weak_topics": user_profile.get("weaknesses", []),
            "topic_stats": {},
        }
    else:
        assessment_summary = lang_result

    # 重新做一次知识库检索（确保最新）
    profile_text = json.dumps(user_profile, ensure_ascii=False)
    knowledge_matches = []
    try:
        search_parts = []
        if user_profile.get("tags"):
            search_parts.append(" ".join(user_profile["tags"]))
        if user_profile.get("weaknesses"):
            search_parts.append(" ".join(user_profile["weaknesses"]))
        search_query = " ".join(search_parts) if search_parts else user_profile.get("summary", "")
        if search_query:
            knowledge_matches = knowledge_base.search(search_query, k=10)
    except Exception as e:
        print(f"[Plan] 知识库检索失败: {e}")

    # LLM 生成个性化学习计划
    plan = await profile_service.generate_plan(
        profile=user_profile,
        assessment_result=assessment_summary,
        knowledge_matches=knowledge_matches,
    )
    _last_plan[user_id] = plan

    return {
        "profile": user_profile,
        "plan": plan,
        "knowledge_count": len(knowledge_matches),
        "has_assessment": lang_result is not None,
    }


@router.get("/profile/latest")
async def get_latest_profile(user_id: str = Query("default")):
    """获取最近生成的人物画像"""
    user_profile = _last_profile.get(user_id)
    if user_profile is None:
        return {"status": "no_profile"}
    return {"profile": user_profile}
