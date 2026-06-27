from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import List, Dict
from orchestrator import orchestrator
from services.achievement import record_chat

router = APIRouter()


class ChatRequest(BaseModel):
    message: str
    history: List[Dict[str, str]] = []
    language: str = "python"
    user_id: str = "default"


@router.post("/chat")
async def chat(request: ChatRequest):
    """流式对话接口，由 AgentOrchestrator 按意图自动路由"""
    # 记录成就（每次对话触发）
    try:
        record_chat(request.user_id)
    except Exception:
        pass

    async def generate():
        async for chunk in orchestrator.route(request.history, request.message, request.language):
            yield chunk

    return StreamingResponse(
        generate(),
        media_type="text/plain; charset=utf-8"
    )
