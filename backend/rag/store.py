"""ChromaDB 向量存储封装"""
import os
import chromadb
from chromadb.config import Settings

CHROMA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "chroma")

os.makedirs(CHROMA_DIR, exist_ok=True)

_client = chromadb.PersistentClient(
    path=CHROMA_DIR,
    settings=Settings(anonymized_telemetry=False)
)


def get_collection(name: str):
    """获取或创建 Collection"""
    return _client.get_or_create_collection(name=name)


def list_collections():
    return _client.list_collections()


# 预定义三个知识库 Collection 名称
KNOWLEDGE_BASE_COLLECTION = "knowledge_base"
EXERCISE_BANK_COLLECTION = "exercise_bank"
USER_MEMORY_COLLECTION = "user_memory"


def reset_collection(name: str):
    """重置指定知识库"""
    try:
        _client.delete_collection(name=name)
    except Exception:
        pass
    return get_collection(name)
