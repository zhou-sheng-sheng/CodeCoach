"""用户学习进度模型"""
import uuid
from datetime import datetime
from sqlalchemy import String, DateTime, Integer, Float, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column
from models.database import Base


class UserProgress(Base):
    __tablename__ = "user_progress"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id"), nullable=False, default="default")
    topic: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    exercises_attempted: Mapped[int] = mapped_column(Integer, default=0)
    exercises_correct: Mapped[int] = mapped_column(Integer, default=0)
    mastery_score: Mapped[float] = mapped_column(Float, default=0.0)  # 0-100
    last_exercise_id: Mapped[str | None] = mapped_column(String(36), nullable=True)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class ExerciseAttempt(Base):
    __tablename__ = "exercise_attempts"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id"), nullable=False, default="default")
    exercise_id: Mapped[str] = mapped_column(String(36), ForeignKey("exercises.id"), nullable=False)
    user_code: Mapped[str] = mapped_column(Text, nullable=True)
    is_correct: Mapped[bool] = mapped_column(Integer, default=False)  # SQLite 无 bool 类型
    score: Mapped[int] = mapped_column(Integer, default=0)
    feedback: Mapped[str | None] = mapped_column(Text, nullable=True)
    attempt_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
