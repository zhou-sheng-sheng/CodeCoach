"""向量嵌入服务 — 使用阿里百炼 DashScope text-embedding-v3 API"""
import os
import time
from http import HTTPStatus
from dashscope import TextEmbedding
from langchain_core.embeddings import Embeddings

DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY", "")
EMBED_MODEL = os.getenv("EMBED_MODEL", "text-embedding-v3")

BATCH_SIZE = 10
MAX_RETRIES = 3
RETRY_DELAY = 1.0


class DashScopeEmbeddings(Embeddings):
    def embed_documents(self, texts):
        all_embeddings = []
        for i in range(0, len(texts), BATCH_SIZE):
            batch = texts[i:i + BATCH_SIZE]
            for attempt in range(MAX_RETRIES):
                try:
                    resp = TextEmbedding.call(
                        model=EMBED_MODEL,
                        input=batch,
                        api_key=DASHSCOPE_API_KEY,
                    )
                    if resp.status_code == HTTPStatus.OK:
                        all_embeddings.extend(
                            [emb["embedding"] for emb in resp.output["embeddings"]]
                        )
                        break
                    else:
                        print(f"[Embedder] API error (attempt {attempt+1}): {resp.message}")
                        raise RuntimeError(resp.message)
                except Exception as e:
                    if attempt == MAX_RETRIES - 1:
                        raise RuntimeError(f"Embedding API failed after {MAX_RETRIES} retries: {e}")
                    time.sleep(RETRY_DELAY * (attempt + 1))
        return all_embeddings

    def embed_query(self, text):
        embeddings = self.embed_documents([text])
        return embeddings[0]


class Embedder:
    def __init__(self):
        self._embeddings = None
        self._initialized = False

    def _lazy_init(self):
        if self._initialized:
            return
        if not DASHSCOPE_API_KEY:
            print("[Embedder] 未设置 DASHSCOPE_API_KEY，向量嵌入功能不可用")
            self._initialized = True
            return
        print(f"[Embedder] 使用阿里百炼模型: {EMBED_MODEL}")
        self._embeddings = DashScopeEmbeddings()
        print(f"[Embedder] 初始化完成，批量大小: {BATCH_SIZE}")
        self._initialized = True

    def embed(self, texts):
        self._lazy_init()
        if self._embeddings is None:
            raise RuntimeError("Embedder not available: DASHSCOPE_API_KEY not set")
        return self._embeddings.embed_documents(texts)

    def embed_query(self, text):
        self._lazy_init()
        if self._embeddings is None:
            raise RuntimeError("Embedder not available: DASHSCOPE_API_KEY not set")
        return self._embeddings.embed_query(text)

    @property
    def embeddings(self):
        self._lazy_init()
        if self._embeddings is None:
            raise RuntimeError("Embedder not available: DASHSCOPE_API_KEY not set")
        return self._embeddings


embedder = Embedder()
