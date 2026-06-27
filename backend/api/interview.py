"""模拟面试 API"""
from fastapi import APIRouter
from pydantic import BaseModel
from agents.interview_agent import interview_agent

router = APIRouter(prefix="/api/interview")


class StartRequest(BaseModel):
    interview_type: str = "algorithm"  # algorithm | system_design | behavioral
    language: str = "python"
    user_id: str = "default"


class AnswerRequest(BaseModel):
    session_id: str
    answer: str


class ActionRequest(BaseModel):
    session_id: str


@router.post("/start")
async def start_interview(req: StartRequest):
    """开始面试——创建会话并出第一题"""
    if req.interview_type not in ("algorithm", "system_design", "behavioral"):
        return {"error": f"不支持的面试类型: {req.interview_type}"}

    session = interview_agent.create_session(req.interview_type, req.language, req.user_id)
    result = interview_agent.start_question(session.session_id)
    return result


@router.post("/answer")
async def submit_answer(req: AnswerRequest):
    """提交回答——评分并触发追问或进入下一题"""
    session = interview_agent.get_session(req.session_id)
    if not session:
        return {"error": "会话不存在或已过期"}

    if session.phase == "follow_up":
        return interview_agent.answer_follow_up(req.session_id, req.answer)
    else:
        return interview_agent.evaluate_answer(req.session_id, req.answer)


@router.post("/next")
async def next_question(req: ActionRequest):
    """进入下一题（评分展示后调用）"""
    return interview_agent.get_next(req.session_id)


@router.post("/skip")
async def skip_follow_ups(req: ActionRequest):
    """跳过追问，直接进入评分"""
    return interview_agent.skip_follow_ups(req.session_id)


@router.get("/status/{session_id}")
async def interview_status(session_id: str):
    """获取面试状态"""
    s = interview_agent.get_session(session_id)
    if not s:
        return {"error": "会话不存在"}
    return {
        "session_id": s.session_id,
        "phase": s.phase,
        "current_question": s.current_q_index + 1,
        "total_questions": len(s.questions),
        "scores": s.scores,
    }


@router.get("/types")
async def interview_types():
    """获取支持的面试类型"""
    return {
        "types": [
            {
                "key": "algorithm",
                "label": "算法面试",
                "description": "随机出算法题 → 限时作答 → 追问复杂度 → 综合评分。适合准备技术面试算法轮。",
                "icon": "code",
            },
            {
                "key": "system_design",
                "label": "系统设计面试",
                "description": "给定设计场景 → 引导式讨论 → 评估架构方案。适合中高级工程师面试准备。",
                "icon": "architecture",
            },
            {
                "key": "behavioral",
                "label": "行为面试",
                "description": "STAR 法则引导 → 模拟真实面试官追问。适合准备软技能面试轮。",
                "icon": "people",
            },
        ]
    }
