"""代码沙箱 API — 在线运行代码"""
from fastapi import APIRouter
from pydantic import BaseModel
from sandbox import run_python, run_javascript
from services.achievement import record_sandbox_run

router = APIRouter(prefix="/api/sandbox")


class RunRequest(BaseModel):
    code: str
    language: str = "python"
    stdin: str = ""
    user_id: str = "default"


LANGUAGE_RUNNERS = {
    "python": run_python,
    "py": run_python,
    "javascript": run_javascript,
    "js": run_javascript,
    "typescript": run_javascript,
    "ts": run_javascript,
    "node": run_javascript,
}


@router.post("/run")
async def run_code(req: RunRequest):
    """在沙箱中执行代码"""
    runner = LANGUAGE_RUNNERS.get(req.language.lower())
    if not runner:
        return {
            "success": False,
            "error": f"不支持的语言: {req.language}，当前支持: python, javascript",
            "stdout": "",
            "stderr": "",
            "exit_code": -1,
            "timed_out": False,
        }
    result = runner(req.code, req.stdin)
    # 记录成就
    if result.get("success") or result.get("exit_code") is not None:
        new_ach = record_sandbox_run(req.user_id)
        result["new_achievements"] = new_ach
    return result
