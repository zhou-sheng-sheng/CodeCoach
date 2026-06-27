from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import List, Dict, Optional
from agents.review_agent import ReviewAgent

router = APIRouter()

review_agent = ReviewAgent()


class ReviewRequest(BaseModel):
    code: str
    language: str = ""
    file_path: str = ""


@router.post("/review")
async def review_code(request: ReviewRequest):
    """代码审查接口 — 流式返回审查结果"""

    async def generate():
        if request.file_path:
            async for chunk in review_agent.review_file(
                file_path=request.file_path,
                content=request.code
            ):
                yield chunk
        else:
            async for chunk in review_agent.review(
                code=request.code,
                language=request.language
            ):
                yield chunk

    return StreamingResponse(
        generate(),
        media_type="text/plain; charset=utf-8"
    )
