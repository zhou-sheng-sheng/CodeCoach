"""习题练习 API — 出题 + 提交评分"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
from services.exercise_service import get_exercises, grade_exercises
from services.achievement import record_exercise

router = APIRouter(prefix="/api/exercises")


class StartRequest(BaseModel):
    language: str = "python"
    topic: Optional[str] = None
    difficulty: Optional[str] = None
    count: int = 10


class SubmitRequest(BaseModel):
    language: str = "python"
    answers: dict[str, int] = {}
    user_id: str = "default"


@router.post("/start")
async def start_exercises(req: StartRequest):
    """获取习题（按条件筛选）"""
    questions = get_exercises(
        language=req.language,
        topic=req.topic,
        difficulty=req.difficulty,
        count=req.count,
    )
    return {
        "language": req.language,
        "total": len(questions),
        "questions": questions,
    }


@router.post("/submit")
async def submit_exercises(req: SubmitRequest):
    """提交答案，返回评分和详情"""
    result = grade_exercises(req.language, req.answers)
    # 记录成就
    total = result.get("total", len(req.answers))
    correct = result.get("correct", 0)
    new_ach = record_exercise(total, correct, req.user_id)
    result["new_achievements"] = new_ach
    return result
