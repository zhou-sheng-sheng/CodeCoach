"""错题本服务 — 错题记录、累计、统计"""

import json
import os
from datetime import datetime
from data_utils import get_user_data_path, ensure_user_dir, migrate_global_data_if_needed


def _error_book_file(user_id: str) -> str:
    return get_user_data_path(user_id, "error_book.json")


def _ensure_data_file(user_id: str) -> dict:
    """确保数据目录和文件存在，返回已加载的数据"""
    ensure_user_dir(user_id)
    migrate_global_data_if_needed(user_id)
    filepath = _error_book_file(user_id)
    if not os.path.exists(filepath):
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("{}")
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}


def _save_data(data: dict, user_id: str) -> None:
    """保存数据到 JSON 文件"""
    ensure_user_dir(user_id)
    filepath = _error_book_file(user_id)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def record_error(language: str, question: dict, user_id: str = "default") -> dict:
    """
    记录一道错题。
    - 如果该题 ID 已存在：error_count += 1，更新 last_error_time
    - 如果不存在：新增记录，error_count = 1，记录 first/last_error_time
    - 返回更新后的记录
    """
    data = _ensure_data_file(user_id)
    lang_key = language

    if lang_key not in data:
        data[lang_key] = {}

    qid = question.get("id", "")
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if qid in data[lang_key]:
        # 已存在：累加
        entry = data[lang_key][qid]
        entry["error_count"] = entry.get("error_count", 0) + 1
        entry["last_error_time"] = now
        # 如果题库中题目有更新（如选项有变化），可选择不覆盖原始字段
    else:
        # 新增
        entry = {
            "question": question.get("question", ""),
            "options": question.get("options", []),
            "answer": question.get("answer", -1),
            "topic": question.get("topic", ""),
            "difficulty": question.get("difficulty", ""),
            "explanation": question.get("explanation", ""),
            "error_count": 1,
            "first_error_time": now,
            "last_error_time": now,
        }
    data[lang_key][qid] = entry
    _save_data(data, user_id)
    return dict(entry)


def get_error_book(language: str | None = None, user_id: str = "default") -> dict:
    """获取整个错题本或指定语言"""
    data = _ensure_data_file(user_id)
    if language:
        return data.get(language, {})
    return data


def get_error_stats(language: str, user_id: str = "default") -> dict:
    """
    错题统计：
    - total_errors: 错题总数（不重复题目数）
    - total_attempts: 累计错误次数
    - by_topic: {topic: {count, attempts}}
    - by_difficulty: {difficulty: {count, attempts}}
    - most_wrong: [{question_id, error_count}] (TOP 5)
    """
    lang_data = get_error_book(language, user_id)

    total_errors = len(lang_data)
    total_attempts = sum(e.get("error_count", 0) for e in lang_data.values())

    by_topic: dict[str, dict] = {}
    by_difficulty: dict[str, dict] = {}

    for qid, entry in lang_data.items():
        topic = entry.get("topic", "未分类")
        diff = entry.get("difficulty", "未知")
        ec = entry.get("error_count", 0)

        if topic not in by_topic:
            by_topic[topic] = {"count": 0, "attempts": 0}
        by_topic[topic]["count"] += 1
        by_topic[topic]["attempts"] += ec

        if diff not in by_difficulty:
            by_difficulty[diff] = {"count": 0, "attempts": 0}
        by_difficulty[diff]["count"] += 1
        by_difficulty[diff]["attempts"] += ec

    # TOP 5 高频错题
    sorted_errors = sorted(
        lang_data.items(),
        key=lambda item: item[1].get("error_count", 0),
        reverse=True
    )
    most_wrong = [
        {
            "question_id": qid,
            "question": entry.get("question", ""),
            "topic": entry.get("topic", "未分类"),
            "error_count": entry.get("error_count", 0),
        }
        for qid, entry in sorted_errors[:5]
    ]

    return {
        "total_errors": total_errors,
        "total_attempts": total_attempts,
        "by_topic": by_topic,
        "by_difficulty": by_difficulty,
        "most_wrong": most_wrong,
    }
