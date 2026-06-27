"""用户记忆库 — 存储用户对话摘要、薄弱点、学习偏好等个性化信息"""
import uuid
import json
from datetime import datetime
from rag.embedder import embedder
from rag.store import get_collection, USER_MEMORY_COLLECTION as COLLECTION_NAME


class UserMemory:
    """用户个性化记忆向量库"""

    def __init__(self):
        self.collection = get_collection(COLLECTION_NAME)

    def remember(self, user_id: str, content: str, memory_type: str = "conversation", metadata: dict | None = None):
        """存储一条记忆"""
        doc_id = str(uuid.uuid4())
        meta = {
            "user_id": user_id,
            "memory_type": memory_type,  # conversation / weakness / preference / achievement
            "timestamp": datetime.utcnow().isoformat(),
        }
        if metadata:
            meta.update(metadata)

        embeddings = embedder.embed([content])
        self.collection.add(
            documents=[content],
            metadatas=[meta],
            embeddings=embeddings,
            ids=[doc_id]
        )
        return doc_id

    def recall(self, user_id: str, query: str, k: int = 5, memory_type: str | None = None) -> list[dict]:
        """检索相关记忆"""
        query_embedding = embedder.embed_query(query)

        where_filter: dict = {"user_id": user_id}
        if memory_type:
            where_filter = {"$and": [{"user_id": user_id}, {"memory_type": memory_type}]}

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=k,
            where=where_filter
        )

        out = []
        if results["ids"] and results["ids"][0]:
            for i, doc_id in enumerate(results["ids"][0]):
                out.append({
                    "id": doc_id,
                    "content": results["documents"][0][i],
                    "metadata": results["metadatas"][0][i] if results["metadatas"] else {},
                    "distance": results["distances"][0][i] if results["distances"] else 0,
                })
        return out

    def get_weaknesses(self, user_id: str, k: int = 5) -> list[str]:
        """获取用户薄弱点"""
        results = self.collection.get(
            where={"$and": [{"user_id": user_id}, {"memory_type": "weakness"}]},
            limit=k
        )
        return results["documents"] if results["documents"] else []

    def get_profile_context(self, user_id: str) -> str:
        """获取用户画像上下文（用于注入到 Agent prompt）"""
        weaknesses = self.get_weaknesses(user_id, k=3)
        profile = self.recall(user_id, "学习偏好 编程背景 目标", k=5, memory_type="preference")

        parts = []
        if weaknesses:
            parts.append("## 用户薄弱环节\n" + "\n".join(f"- {w}" for w in weaknesses))
        if profile:
            parts.append("## 用户偏好\n" + "\n".join(
                f"- {m['content']}" for m in profile
            ))

        return "\n\n".join(parts) if parts else ""

    def count(self, user_id: str | None = None) -> int:
        if user_id:
            results = self.collection.get(where={"user_id": user_id})
            return len(results["ids"]) if results["ids"] else 0
        return self.collection.count()

    def reset(self):
        try:
            self.collection._client.delete_collection(name=COLLECTION_NAME)
        except Exception:
            pass
        self.collection = get_collection(COLLECTION_NAME)


user_memory = UserMemory()
