"""重建 ChromaDB 三个知识库 collection，使用百炼 embedding 重新灌入种子数据。
用法: python rebuild_collections.py
前提: 已设置 DASHSCOPE_API_KEY 环境变量
"""
import sys
sys.path.insert(0, r"E:\编程AI陪练系统\backend")

from rag.store import (
    reset_collection,
    KNOWLEDGE_BASE_COLLECTION,
    EXERCISE_BANK_COLLECTION,
    USER_MEMORY_COLLECTION,
)
from rag.embedder import embedder

from rag.knowledge_base import SEED_KNOWLEDGE
from rag.exercise_bank import SEED_EXERCISES

BATCH_SIZE = 10


def rebuild(name, seeds, add_fn):
    print(f"[rebuild] 重置 {name} ...")
    collection = reset_collection(name)
    total = len(seeds)
    for i in range(0, total, BATCH_SIZE):
        batch = seeds[i:i + BATCH_SIZE]
        add_fn(batch)
        print(f"[rebuild] {name}: {min(i+BATCH_SIZE, total)}/{total}")
    print(f"[rebuild] {name} 完成，总数 {total}")


# ---- knowledge_base ----
def _add_kb_batch(batch):
    import uuid
    from rag.store import get_collection, KNOWLEDGE_BASE_COLLECTION
    col = get_collection(KNOWLEDGE_BASE_COLLECTION)
    texts = [item["text"] for item in batch]
    ids = [str(uuid.uuid4()) for _ in texts]
    metadatas = [
        {"topic": item.get("topic", ""), "language": item.get("language", "通用")}
        for item in batch
    ]
    embeddings = embedder.embed(texts)
    col.add(documents=texts, metadatas=metadatas, embeddings=embeddings, ids=ids)


# ---- exercise_bank ----
def _add_ex_batch(batch):
    import uuid
    from rag.store import get_collection, EXERCISE_BANK_COLLECTION
    col = get_collection(EXERCISE_BANK_COLLECTION)
    texts = [ex["text"] for ex in batch]
    ids = [str(uuid.uuid4()) for _ in texts]
    metadatas = [
        {
            "difficulty": ex.get("difficulty", "medium"),
            "topic": ex.get("topic", ""),
            "language": ex.get("language", "python"),
            "exercise_type": ex.get("exercise_type", "code_writing"),
        }
        for ex in batch
    ]
    embeddings = embedder.embed(texts)
    col.add(documents=texts, metadatas=metadatas, embeddings=embeddings, ids=ids)


if __name__ == "__main__":
    # user_memory 无种子数据，仅重建空 collection
    print("[rebuild] 重置 user_memory（无种子数据）...")
    reset_collection(USER_MEMORY_COLLECTION)
    print("[rebuild] user_memory 完成，总数 0")

    rebuild(KNOWLEDGE_BASE_COLLECTION, SEED_KNOWLEDGE, _add_kb_batch)
    rebuild(EXERCISE_BANK_COLLECTION, SEED_EXERCISES, _add_ex_batch)
    print("[rebuild] 全部完成")
