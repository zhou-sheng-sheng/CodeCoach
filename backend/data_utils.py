"""
用户数据隔离工具模块

提供按 user_id 分目录存储数据文件的能力，
支持首次访问时自动迁移旧的全局数据。
"""
import os
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

# 需要迁移的全局数据文件名列表
_MIGRATABLE_FILES = [
    "assessment_result.json",
    "achievements.json",
    "error_book.json",
    "user_profile.json",
]


def _resolve_user_id(user_id: str) -> str:
    """处理空/None user_id，兜底为 default"""
    return user_id.strip() if user_id and user_id.strip() else "default"


def get_user_data_dir(user_id: str) -> str:
    """获取指定用户的数据目录路径"""
    return os.path.join(DATA_DIR, _resolve_user_id(user_id))


def get_user_data_path(user_id: str, filename: str) -> str:
    """获取指定用户的某数据文件完整路径"""
    return os.path.join(get_user_data_dir(user_id), filename)


def ensure_user_dir(user_id: str) -> str:
    """确保用户数据目录存在，返回目录路径"""
    user_dir = get_user_data_dir(user_id)
    os.makedirs(user_dir, exist_ok=True)
    return user_dir


def migrate_global_data_if_needed(user_id: str):
    """
    首次切换到某用户时，检查全局 data/ 下是否有旧数据。
    若有且用户目录下不存在对应文件，则复制过去。
    """
    user_id = _resolve_user_id(user_id)
    if user_id == "default":
        return  # default 用户本身就在全局目录，无需迁移

    user_dir = ensure_user_dir(user_id)
    for filename in _MIGRATABLE_FILES:
        global_path = os.path.join(DATA_DIR, filename)
        user_path = os.path.join(user_dir, filename)
        if os.path.exists(global_path) and not os.path.exists(user_path):
            shutil.copy2(global_path, user_path)
