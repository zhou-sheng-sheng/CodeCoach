"""
数据看板聚合服务
从评估结果和错题记录聚合看板所需数据
"""

from services.error_book import get_error_stats


def get_dashboard_data(language: str, assessment_result: dict | None = None, user_id: str = "default") -> dict:
    """聚合看板数据"""
    errors = get_error_stats(language, user_id)

    if assessment_result is None:
        return _empty_dashboard(language, errors)

    score = assessment_result.get("score", 0)
    total_q = assessment_result.get("total", 0)
    correct = assessment_result.get("correct", 0)
    level = assessment_result.get("level", "")
    advice = assessment_result.get("advice", "")
    topic_stats_raw = assessment_result.get("topic_stats", {})
    difficulty_stats_raw = assessment_result.get("difficulty_stats", {})
    weak_topics = assessment_result.get("weak_topics", [])

    # Build topic_stats from raw data (handle list of tuples from pickle-style)
    topic_stats = _normalize_stats(topic_stats_raw)
    difficulty_stats = _normalize_stats(difficulty_stats_raw)

    # Count mastered topics (correct rate >= 80%)
    total_topics = len(topic_stats)
    mastered = sum(1 for s in topic_stats.values()
                   if s["total"] > 0 and s["correct"] / s["total"] >= 0.8)

    # Combine assessment weak topics with error book most_wrong topics
    error_weak = [item.get("topic", "未分类") for item in errors.get("most_wrong", [])[:3]]
    combined_weak = list(dict.fromkeys(weak_topics + error_weak))[:5]

    # Weakest 3 topics
    weakest = combined_weak[:3] if combined_weak else weak_topics[:3] if weak_topics else ["暂无数据"]

    # Generate recommendation
    recommendation = _generate_recommendation(level, weakest, errors.get("total_errors", 0))

    return {
        "has_assessment": True,
        "assessment": {
            "score": score,
            "level": level,
            "advice": advice,
            "correct": correct,
            "total": total_q,
            "topic_stats": topic_stats,
            "difficulty_stats": difficulty_stats,
            "weak_topics": weak_topics,
        },
        "errors": {
            "total_errors": errors.get("total_errors", 0),
            "total_attempts": errors.get("total_attempts", 0),
            "by_topic": errors.get("by_topic", {}),
            "by_difficulty": errors.get("by_difficulty", {}),
            "most_wrong": errors.get("most_wrong", []),
        },
        "summary": {
            "overall_level": level or "未评估",
            "total_topics": total_topics,
            "mastered_topics": mastered,
            "weakest_topics": weakest,
            "recommendation": recommendation,
        },
    }


def _empty_dashboard(language: str, errors: dict) -> dict:
    return {
        "has_assessment": False,
        "assessment": None,
        "errors": {
            "total_errors": errors.get("total_errors", 0),
            "total_attempts": errors.get("total_attempts", 0),
            "by_topic": errors.get("by_topic", {}),
            "by_difficulty": errors.get("by_difficulty", {}),
            "most_wrong": errors.get("most_wrong", []),
        },
        "summary": {
            "overall_level": "未评估",
            "total_topics": 0,
            "mastered_topics": 0,
            "weakest_topics": [],
            "recommendation": "完成基础评估后，这里将展示你的学习数据分析。",
        },
    }


def _normalize_stats(raw: dict) -> dict:
    """将 raw stats 标准化为 {topic: {total, correct}}"""
    result = {}
    if not raw:
        return result
    for k, v in raw.items():
        if isinstance(v, dict):
            result[k] = {"total": v.get("total", 0), "correct": v.get("correct", 0)}
        elif isinstance(v, (list, tuple)) and len(v) >= 2:
            result[k] = {"total": int(v[0]), "correct": int(v[1])}
        else:
            result[k] = {"total": 0, "correct": 0}
    return result


def _generate_recommendation(level: str, weakest: list[str], total_errors: int) -> str:
    if not weakest or weakest == ["暂无数据"]:
        return "继续保持，你已经掌握了大部分知识点！"
    topics = "、".join(weakest)
    if total_errors > 10:
        return f"建议重点复习 {topics} 相关知识点，累计错题较多，可通过专项练习强化。"
    elif level in ("入门",):
        return f"基础阶段建议从 {topics} 入手，逐步建立编程思维。"
    elif level in ("初级",):
        return f"建议针对 {topics} 进行强化训练，巩固基础后向中级迈进。"
    else:
        return f"弱项集中在 {topics}，建议针对性练习以向更高水平突破。"
