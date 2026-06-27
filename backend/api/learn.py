"""学习板块 API — 学习路径 + 知识点 + 关联习题"""
from fastapi import APIRouter
from pydantic import BaseModel
from services.learn_service import get_learning_path, get_lesson, get_lesson_exercises

router = APIRouter(prefix="/api/learn")


class ExercisesRequest(BaseModel):
    count: int = 5
    language: str = "python"


@router.get("/path")
async def learning_path(language: str = "python"):
    """获取学习路径（支持多语言）"""
    return {
        "language": language,
        "topics": get_learning_path(language),
    }


@router.get("/lesson/{lesson_id}")
async def lesson_detail(lesson_id: str, language: str = "python"):
    """获取知识点详情"""
    lesson = get_lesson(lesson_id, language)
    if not lesson:
        return {"error": "知识点不存在", "lesson_id": lesson_id}
    return {"lesson": lesson, "language": language}


@router.post("/exercises/{lesson_id}")
async def lesson_exercises(lesson_id: str, req: ExercisesRequest):
    """获取与知识点相关的练习题"""
    questions = get_lesson_exercises(lesson_id, req.count, req.language)
    return {
        "lesson_id": lesson_id,
        "language": req.language,
        "total": len(questions),
        "questions": questions,
    }
