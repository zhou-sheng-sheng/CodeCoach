"""用户数据模型"""
import uuid
from datetime import datetime
from sqlalchemy import String, Integer, DateTime, Text, Enum as SAEnum
from sqlalchemy.orm import Mapped, mapped_column
from models.database import Base
import enum


class SkillLevel(str, enum.Enum):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"


class FocusArea(str, enum.Enum):
    PYTHON = "python"
    JAVASCRIPT = "javascript"
    JAVA = "java"
    GO = "go"
    RUST = "rust"
    CPP = "cpp"
    ALGORITHM = "algorithm"
    SYSTEM_DESIGN = "system_design"
    WEB = "web"
    DATA = "data"


class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False, default="learner")
    skill_level: Mapped[SkillLevel] = mapped_column(SAEnum(SkillLevel), default=SkillLevel.BEGINNER)
    focus_area: Mapped[FocusArea] = mapped_column(SAEnum(FocusArea), default=FocusArea.PYTHON)
    total_sessions: Mapped[int] = mapped_column(Integer, default=0)
    total_exercises: Mapped[int] = mapped_column(Integer, default=0)
    correct_exercises: Mapped[int] = mapped_column(Integer, default=0)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    last_active: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    preferences: Mapped[str | None] = mapped_column(Text, nullable=True)  # JSON 字符串
