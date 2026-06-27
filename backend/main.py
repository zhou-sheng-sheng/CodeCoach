import json
import os
from dotenv import load_dotenv
# 优先从上级目录加载（开发环境 .env 在项目根目录），不存在则从当前目录加载（打包环境 .env 在 backend/ 内）
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
if not os.getenv("OPENAI_API_KEY"):
    load_dotenv()  # 回退到 CWD（打包环境下 spawn cwd = backend/）

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from api.chat import router as chat_router
from api.review import router as review_router
from api.assessment import router as assessment_router
from api.exercise import router as exercise_router
from api.learn import router as learn_router
from api.errors import router as errors_router
from api.dashboard import router as dashboard_router
from api.sandbox import router as sandbox_router
from api.interview import router as interview_router
from api.achievement import router as achievement_router
from api.auth import router as auth_router
from api.notebook import router as notebook_router


class UTF8JSONResponse(JSONResponse):
    """自定义 JSON 响应：确保中文不被转义为 \\uXXXX，Content-Type 明确声明 UTF-8"""
    media_type = "application/json; charset=utf-8"

    def render(self, content) -> bytes:
        return json.dumps(
            content,
            ensure_ascii=False,
            allow_nan=False,
            indent=None,
            separators=(",", ":"),
        ).encode("utf-8")


app = FastAPI(
    title="编程AI陪练 API",
    version="0.1.0",
    description="多Agent编程学习陪练系统后端",
    default_response_class=UTF8JSONResponse,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router, prefix="/api")
app.include_router(review_router, prefix="/api")
app.include_router(assessment_router)
app.include_router(exercise_router)
app.include_router(learn_router)
app.include_router(errors_router)
app.include_router(dashboard_router)
app.include_router(sandbox_router)
app.include_router(interview_router)
app.include_router(achievement_router)
app.include_router(auth_router)
app.include_router(notebook_router)


@app.get("/health")
async def health():
    return {"status": "ok", "version": "0.1.0"}
