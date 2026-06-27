"""习题库模型"""
import uuid
from datetime import datetime
from sqlalchemy import String, Text, Integer, DateTime, Enum as SAEnum
from sqlalchemy.orm import Mapped, mapped_column
from models.database import Base
import enum


class Difficulty(str, enum.Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


class ExerciseType(str, enum.Enum):
    MULTIPLE_CHOICE = "multiple_choice"
    CODE_WRITING = "code_writing"
    DEBUGGING = "debugging"
    CODE_REVIEW = "code_review"
    FILL_BLANK = "fill_blank"


class Exercise(Base):
    __tablename__ = "exercises"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    difficulty: Mapped[Difficulty] = mapped_column(SAEnum(Difficulty), nullable=False)
    exercise_type: Mapped[ExerciseType] = mapped_column(SAEnum(ExerciseType), nullable=False)
    topic: Mapped[str] = mapped_column(String(100), nullable=False, index=True)  # e.g. "闭包", "链表"
    language: Mapped[str] = mapped_column(String(30), nullable=False, default="python")
    content: Mapped[str] = mapped_column(Text, nullable=False)  # 题目描述
    starter_code: Mapped[str | None] = mapped_column(Text, nullable=True)
    answer: Mapped[str | None] = mapped_column(Text, nullable=True)
    explanation: Mapped[str | None] = mapped_column(Text, nullable=True)
    tags: Mapped[str | None] = mapped_column(String(300), nullable=True)  # 逗号分隔
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
