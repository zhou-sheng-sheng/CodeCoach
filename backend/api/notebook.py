"""
笔记 API — 按用户 ID 隔离，存储为 data/{user_id}/notebook.json
"""
import os
import json
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from typing import Optional

from data_utils import ensure_user_dir, get_user_data_path

router = APIRouter(prefix="/api/notebook", tags=["notebook"])


class NoteSaveRequest(BaseModel):
    user_id: str = "default"
    title: str
    content: str
    topic: str = ""


class NoteUpdateRequest(BaseModel):
    user_id: str = "default"
    title: Optional[str] = None
    content: Optional[str] = None
    topic: Optional[str] = None


def _load_notes(user_id: str) -> list:
    """加载指定用户的笔记列表"""
    path = get_user_data_path(user_id, "notebook.json")
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []


def _save_notes(user_id: str, notes: list):
    """保存指定用户的笔记列表"""
    ensure_user_dir(user_id)
    path = get_user_data_path(user_id, "notebook.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(notes, f, ensure_ascii=False, indent=2)


# ── 工具函数：时间戳 + 简易雪花 ID ──
import time
import random

def _make_id() -> str:
    """生成简易唯一 ID"""
    return str(int(time.time() * 1000)) + str(random.randint(1000, 9999))


@router.post("")
async def create_note(req: NoteSaveRequest):
    """创建新笔记"""
    notes = _load_notes(req.user_id)
    now = int(time.time() * 1000)
    note = {
        "id": _make_id(),
        "title": req.title.strip(),
        "content": req.content,
        "topic": req.topic.strip(),
        "created_at": now,
        "updated_at": now,
    }
    notes.insert(0, note)
    _save_notes(req.user_id, notes)
    return {"success": True, "note": note}


@router.get("")
async def list_notes(user_id: str = Query("default")):
    """获取用户笔记列表"""
    notes = _load_notes(user_id)
    return {"success": True, "notes": notes}


@router.put("/{note_id}")
async def update_note(note_id: str, req: NoteUpdateRequest):
    """更新笔记"""
    notes = _load_notes(req.user_id)
    for note in notes:
        if note["id"] == note_id:
            if req.title is not None:
                note["title"] = req.title.strip()
            if req.content is not None:
                note["content"] = req.content
            if req.topic is not None:
                note["topic"] = req.topic.strip()
            note["updated_at"] = int(time.time() * 1000)
            _save_notes(req.user_id, notes)
            return {"success": True, "note": note}
    raise HTTPException(status_code=404, detail="笔记不存在")


@router.delete("/{note_id}")
async def delete_note(note_id: str, user_id: str = Query("default")):
    """删除笔记"""
    notes = _load_notes(user_id)
    original_len = len(notes)
    notes = [n for n in notes if n["id"] != note_id]
    if len(notes) == original_len:
        raise HTTPException(status_code=404, detail="笔记不存在")
    _save_notes(user_id, notes)
    return {"success": True}
