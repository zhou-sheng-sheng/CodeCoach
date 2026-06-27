"""对话记录模型"""
import uuid
from datetime import datetime
from sqlalchemy import String, Text, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from models.database import Base


class Conversation(Base):
    __tablename__ = "conversations"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id"), nullable=False, default="default")
    session_id: Mapped[str] = mapped_column(String(36), nullable=False, index=True)
    role: Mapped[str] = mapped_column(String(10), nullable=False)  # 'user' | 'assistant'
    content: Mapped[str] = mapped_column(Text, nullable=False)
    routed_agent: Mapped[str | None] = mapped_column(String(30), nullable=True)  # 'coach' | 'reviewer'
    source_knowledge: Mapped[str | None] = mapped_column(Text, nullable=True)  # RAG 检索到的知识片段
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, index=True)
