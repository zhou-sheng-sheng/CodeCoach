"""成就系统服务 — 成就定义 + 解锁规则"""
import json
import os
from datetime import datetime, date
from typing import Any
from data_utils import get_user_data_path, ensure_user_dir, migrate_global_data_if_needed


# ─── 成就定义 ────────────────────────────────────────────

ACHIEVEMENT_DEFINITIONS: list[dict[str, Any]] = [
    # 学习里程碑
    {
        "id": "first_chat",
        "name": "初次对话",
        "description": "完成第一次 AI 对话陪练",
        "icon": "chat",
        "category": "milestone",
        "rarity": "common",
    },
    {
        "id": "chat_10",
        "name": "勤学好问",
        "description": "累计完成 10 次 AI 对话",
        "icon": "chat",
        "category": "milestone",
        "rarity": "uncommon",
    },
    {
        "id": "chat_50",
        "name": "求知若渴",
        "description": "累计完成 50 次 AI 对话",
        "icon": "chat",
        "category": "milestone",
        "rarity": "rare",
    },
    # 评估成就
    {
        "id": "first_assessment",
        "name": "初出茅庐",
        "description": "完成第一次基础评估",
        "icon": "assessment",
        "category": "milestone",
        "rarity": "common",
    },
    {
        "id": "assessment_80",
        "name": "高分选手",
        "description": "评估得分达到 80 分以上",
        "icon": "assessment",
        "category": "skill",
        "rarity": "uncommon",
    },
    {
        "id": "assessment_100",
        "name": "满分达人",
        "description": "评估获得满分",
        "icon": "assessment",
        "category": "skill",
        "rarity": "legendary",
    },
    # 习题成就
    {
        "id": "exercise_10",
        "name": "初试身手",
        "description": "累计完成 10 道习题",
        "icon": "exercise",
        "category": "milestone",
        "rarity": "common",
    },
    {
        "id": "exercise_50",
        "name": "刷题达人",
        "description": "累计完成 50 道习题",
        "icon": "exercise",
        "category": "milestone",
        "rarity": "uncommon",
    },
    {
        "id": "exercise_100",
        "name": "百题斩",
        "description": "累计完成 100 道习题",
        "icon": "exercise",
        "category": "milestone",
        "rarity": "rare",
    },
    {
        "id": "exercise_perfect",
        "name": "完美表现",
        "description": "单次练习全部正确（至少 5 题）",
        "icon": "exercise",
        "category": "skill",
        "rarity": "rare",
    },
    # 面试成就
    {
        "id": "first_interview",
        "name": "初入职场",
        "description": "完成第一次模拟面试",
        "icon": "interview",
        "category": "milestone",
        "rarity": "common",
    },
    {
        "id": "interview_80",
        "name": "面试达人",
        "description": "模拟面试平均分达到 80 分以上",
        "icon": "interview",
        "category": "skill",
        "rarity": "rare",
    },
    {
        "id": "interview_all_types",
        "name": "全能面试王",
        "description": "完成全部三种面试类型（算法/系统设计/行为）",
        "icon": "interview",
        "category": "skill",
        "rarity": "epic",
    },
    # 学习坚持
    {
        "id": "streak_3",
        "name": "三天打鱼",
        "description": "连续学习 3 天",
        "icon": "streak",
        "category": "streak",
        "rarity": "common",
    },
    {
        "id": "streak_7",
        "name": "一周坚持",
        "description": "连续学习 7 天",
        "icon": "streak",
        "category": "streak",
        "rarity": "uncommon",
    },
    {
        "id": "streak_30",
        "name": "全勤王",
        "description": "连续学习 30 天",
        "icon": "streak",
        "category": "streak",
        "rarity": "legendary",
    },
    # 沙箱成就
    {
        "id": "first_sandbox",
        "name": "初次运行",
        "description": "在沙箱中运行第一次代码",
        "icon": "sandbox",
        "category": "milestone",
        "rarity": "common",
    },
    {
        "id": "sandbox_20",
        "name": "代码狂人",
        "description": "在沙箱中累计运行 20 次代码",
        "icon": "sandbox",
        "category": "milestone",
        "rarity": "uncommon",
    },
]

RARITY_ORDER = ["common", "uncommon", "rare", "epic", "legendary"]
RARITY_LABELS = {
    "common": "普通",
    "uncommon": "稀有",
    "rare": "珍贵",
    "epic": "史诗",
    "legendary": "传说",
}
RARITY_COLORS = {
    "common": "#9e9e9e",
    "uncommon": "#4caf50",
    "rare": "#2196f3",
    "epic": "#9c27b0",
    "legendary": "#ff9800",
}


# ─── 数据存取 ────────────────────────────────────────────

def _achievements_file(user_id: str) -> str:
    return get_user_data_path(user_id, "achievements.json")


def _load(user_id: str = "default") -> dict:
    filepath = _achievements_file(user_id)
    migrate_global_data_if_needed(user_id)
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        if "stats" in data and "by_language" not in data["stats"]:
            data["stats"]["by_language"] = {}
        return data
    return {
        "unlocked": {},
        "stats": {
            "total_chats": 0,
            "total_exercises": 0,
            "total_correct": 0,
            "total_sandbox_runs": 0,
            "assessment_high_score": 0,
            "interview_high_score": 0,
            "interview_types_done": [],
            "last_active_date": None,
            "streak_days": 0,
            "by_language": {},
        },
    }


def _save(data: dict, user_id: str = "default"):
    filepath = _achievements_file(user_id)
    ensure_user_dir(user_id)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def _check_and_unlock(data: dict, ach_id: str, user_id: str = "default") -> str | None:
    if ach_id in data["unlocked"]:
        return None

    definition = next((d for d in ACHIEVEMENT_DEFINITIONS if d["id"] == ach_id), None)
    if not definition:
        return None

    stats = data["stats"]
    unlocked = False

    match ach_id:
        case "first_chat":
            unlocked = stats["total_chats"] >= 1
        case "chat_10":
            unlocked = stats["total_chats"] >= 10
        case "chat_50":
            unlocked = stats["total_chats"] >= 50
        case "first_assessment":
            unlocked = stats.get("assessment_high_score", 0) > 0
        case "assessment_80":
            unlocked = stats.get("assessment_high_score", 0) >= 80
        case "assessment_100":
            unlocked = stats.get("assessment_high_score", 0) >= 100
        case "exercise_10":
            unlocked = stats["total_exercises"] >= 10
        case "exercise_50":
            unlocked = stats["total_exercises"] >= 50
        case "exercise_100":
            unlocked = stats["total_exercises"] >= 100
        case "exercise_perfect":
            unlocked = stats.get("total_correct", 0) >= 5 and stats.get("total_exercises", 0) >= 5
        case "first_interview":
            unlocked = stats.get("interview_high_score", 0) > 0
        case "interview_80":
            unlocked = stats.get("interview_high_score", 0) >= 80
        case "interview_all_types":
            unlocked = len(stats.get("interview_types_done", [])) >= 3
        case "streak_3":
            unlocked = stats.get("streak_days", 0) >= 3
        case "streak_7":
            unlocked = stats.get("streak_days", 0) >= 7
        case "streak_30":
            unlocked = stats.get("streak_days", 0) >= 30
        case "first_sandbox":
            unlocked = stats.get("total_sandbox_runs", 0) >= 1
        case "sandbox_20":
            unlocked = stats.get("total_sandbox_runs", 0) >= 20

    if unlocked:
        data["unlocked"][ach_id] = {
            "unlocked_at": datetime.now().isoformat(),
            "name": definition["name"],
            "rarity": definition["rarity"],
        }
        _save(data, user_id)
        return definition["name"]

    return None


def _update_streak(data: dict, user_id: str = "default"):
    today = date.today().isoformat()
    stats = data["stats"]
    last = stats.get("last_active_date")

    if last == today:
        return

    if last:
        last_date = date.fromisoformat(last)
        days_diff = (date.today() - last_date).days
        if days_diff == 1:
            stats["streak_days"] = stats.get("streak_days", 0) + 1
        elif days_diff > 1:
            stats["streak_days"] = 1
    else:
        stats["streak_days"] = 1

    stats["last_active_date"] = today
    _save(data, user_id)


# ─── 公开 API ────────────────────────────────────────────

def get_all_achievements(user_id: str = "default") -> dict:
    data = _load(user_id)
    unlocked = data["unlocked"]

    result = []
    for ach in ACHIEVEMENT_DEFINITIONS:
        item = {**ach}
        if ach["id"] in unlocked:
            item["unlocked"] = True
            item["unlocked_at"] = unlocked[ach["id"]]["unlocked_at"]
        else:
            item["unlocked"] = False
        result.append(item)

    result.sort(key=lambda x: RARITY_ORDER.index(x["rarity"]) if x["rarity"] in RARITY_ORDER else 99)

    return {
        "achievements": result,
        "stats": {
            "total": len(ACHIEVEMENT_DEFINITIONS),
            "unlocked": len(unlocked),
            "by_rarity": {
                r: sum(1 for a in result if a["rarity"] == r and a.get("unlocked"))
                for r in RARITY_ORDER
            },
            "rarity_labels": RARITY_LABELS,
            "rarity_colors": RARITY_COLORS,
        },
    }


def record_chat(user_id: str = "default") -> list[str]:
    data = _load(user_id)
    data["stats"]["total_chats"] = data["stats"].get("total_chats", 0) + 1
    _update_streak(data, user_id)
    _save(data, user_id)

    data = _load(user_id)
    new_achievements = []
    for ach_id in ["first_chat", "chat_10", "chat_50"]:
        name = _check_and_unlock(data, ach_id, user_id)
        if name:
            new_achievements.append(name)
    for ach_id in ["streak_3", "streak_7", "streak_30"]:
        name = _check_and_unlock(data, ach_id, user_id)
        if name:
            new_achievements.append(name)
    return new_achievements


def record_assessment(score: int, language: str = "python", user_id: str = "default") -> list[str]:
    data = _load(user_id)
    stats = data["stats"]
    by_lang = stats.setdefault("by_language", {})

    lang_entry = by_lang.setdefault(language, {"assessment_high_score": 0})
    if score > lang_entry.get("assessment_high_score", 0):
        lang_entry["assessment_high_score"] = score

    all_high_scores = [v.get("assessment_high_score", 0) for v in by_lang.values()]
    global_high = max(all_high_scores) if all_high_scores else score
    if global_high > stats.get("assessment_high_score", 0):
        stats["assessment_high_score"] = global_high

    _update_streak(data, user_id)
    _save(data, user_id)

    data = _load(user_id)
    new_achievements = []
    for ach_id in ["first_assessment", "assessment_80", "assessment_100"]:
        name = _check_and_unlock(data, ach_id, user_id)
        if name:
            new_achievements.append(name)
    for ach_id in ["streak_3", "streak_7", "streak_30"]:
        name = _check_and_unlock(data, ach_id, user_id)
        if name:
            new_achievements.append(name)
    return new_achievements


def record_exercise(total: int, correct: int, user_id: str = "default") -> list[str]:
    data = _load(user_id)
    data["stats"]["total_exercises"] = data["stats"].get("total_exercises", 0) + total
    data["stats"]["total_correct"] = data["stats"].get("total_correct", 0) + correct
    _update_streak(data, user_id)
    _save(data, user_id)

    data = _load(user_id)
    new_achievements = []
    for ach_id in ["exercise_10", "exercise_50", "exercise_100", "exercise_perfect"]:
        name = _check_and_unlock(data, ach_id, user_id)
        if name:
            new_achievements.append(name)
    for ach_id in ["streak_3", "streak_7", "streak_30"]:
        name = _check_and_unlock(data, ach_id, user_id)
        if name:
            new_achievements.append(name)
    return new_achievements


def record_interview(score: float, interview_type: str, user_id: str = "default") -> list[str]:
    data = _load(user_id)
    if score > data["stats"].get("interview_high_score", 0):
        data["stats"]["interview_high_score"] = int(score)

    types_done = data["stats"].get("interview_types_done", [])
    if interview_type not in types_done:
        types_done.append(interview_type)
        data["stats"]["interview_types_done"] = types_done

    _update_streak(data, user_id)
    _save(data, user_id)

    data = _load(user_id)
    new_achievements = []
    for ach_id in ["first_interview", "interview_80", "interview_all_types"]:
        name = _check_and_unlock(data, ach_id, user_id)
        if name:
            new_achievements.append(name)
    for ach_id in ["streak_3", "streak_7", "streak_30"]:
        name = _check_and_unlock(data, ach_id, user_id)
        if name:
            new_achievements.append(name)
    return new_achievements


def record_sandbox_run(user_id: str = "default") -> list[str]:
    data = _load(user_id)
    data["stats"]["total_sandbox_runs"] = data["stats"].get("total_sandbox_runs", 0) + 1
    _update_streak(data, user_id)
    _save(data, user_id)

    data = _load(user_id)
    new_achievements = []
    for ach_id in ["first_sandbox", "sandbox_20"]:
        name = _check_and_unlock(data, ach_id, user_id)
        if name:
            new_achievements.append(name)
    return new_achievements


def get_stats(language: str = "", user_id: str = "default") -> dict:
    data = _load(user_id)
    stats = data["stats"]
    result = {
        "total_chats": stats.get("total_chats", 0),
        "total_exercises": stats.get("total_exercises", 0),
        "total_correct": stats.get("total_correct", 0),
        "total_sandbox_runs": stats.get("total_sandbox_runs", 0),
        "assessment_high_score": stats.get("assessment_high_score", 0),
        "interview_high_score": stats.get("interview_high_score", 0),
        "interview_types_done": stats.get("interview_types_done", []),
        "streak_days": stats.get("streak_days", 0),
        "by_language": stats.get("by_language", {}),
    }
    if language:
        result["current_language"] = language
        result["lang_stats"] = stats.get("by_language", {}).get(language, {})
    return result
