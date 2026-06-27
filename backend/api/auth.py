"""
用户认证 API
"""
import os
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/api/auth", tags=["auth"])

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data", "users")


class RegisterRequest(BaseModel):
    username: str
    password: str
    confirm_password: str


@router.post("/register")
async def register(req: RegisterRequest):
    username = req.username.strip()
    password = req.password
    confirm_password = req.confirm_password

    if not username:
        raise HTTPException(status_code=400, detail="用户名不能为空")
    if len(password) < 6:
        raise HTTPException(status_code=400, detail="密码长度不能少于6位")
    if password != confirm_password:
        raise HTTPException(status_code=400, detail="两次输入的密码不一致")

    user_dir = os.path.join(DATA_DIR, username)
    if os.path.exists(user_dir):
        raise HTTPException(status_code=400, detail="用户名已存在")

    os.makedirs(user_dir, exist_ok=True)
    return {"success": True, "message": "注册成功"}
