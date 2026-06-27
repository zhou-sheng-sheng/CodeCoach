"""成就系统 API — 成就列表 / 统计数据"""
from fastapi import APIRouter, Query

from services.achievement import (
    get_all_achievements,
    get_stats,
    record_chat,
    record_assessment,
    record_exercise,
    record_interview,
    record_sandbox_run,
)

router = APIRouter(prefix="/api/achievements", tags=["achievements"])


@router.get("")
async def list_achievements(user_id: str = Query("default")):
    """获取所有成就及解锁状态"""
    try:
        return get_all_achievements(user_id)
    except Exception as e:
        return {"error": str(e)}


@router.get("/stats")
async def learning_stats(language: str = Query(""), user_id: str = Query("default")):
    """获取学习统计数据，支持按语言过滤"""
    try:
        return get_stats(language, user_id)
    except Exception as e:
        return {"error": str(e)}


@router.post("/record/chat")
async def record_chat_api(user_id: str = Query("default")):
    """记录一次对话"""
    try:
        new_achievements = record_chat(user_id)
        return {"ok": True, "new_achievements": new_achievements}
    except Exception as e:
        return {"error": str(e)}


@router.post("/record/assessment")
async def record_assessment_api(
    score: int = Query(..., ge=0, le=100),
    language: str = Query("python"),
    user_id: str = Query("default"),
):
    """记录一次评估"""
    try:
        new_achievements = record_assessment(score, language, user_id)
        return {"ok": True, "new_achievements": new_achievements}
    except Exception as e:
        return {"error": str(e)}


@router.post("/record/exercise")
async def record_exercise_api(
    total: int = Query(..., ge=0),
    correct: int = Query(..., ge=0),
    user_id: str = Query("default"),
):
    """记录习题完成"""
    try:
        new_achievements = record_exercise(total, correct, user_id)
        return {"ok": True, "new_achievements": new_achievements}
    except Exception as e:
        return {"error": str(e)}


@router.post("/record/interview")
async def record_interview_api(
    score: float = Query(..., ge=0),
    interview_type: str = Query(...),
    user_id: str = Query("default"),
):
    """记录面试完成"""
    try:
        new_achievements = record_interview(score, interview_type, user_id)
        return {"ok": True, "new_achievements": new_achievements}
    except Exception as e:
        return {"error": str(e)}


@router.post("/record/sandbox")
async def record_sandbox_api(user_id: str = Query("default")):
    """记录沙箱运行"""
    try:
        new_achievements = record_sandbox_run(user_id)
        return {"ok": True, "new_achievements": new_achievements}
    except Exception as e:
        return {"error": str(e)}
