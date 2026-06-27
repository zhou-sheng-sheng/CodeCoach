"""错题本 API"""
from fastapi import APIRouter, Query
from services.error_book import get_error_book, get_error_stats

router = APIRouter(prefix="/api/errors")


@router.get("/book")
async def get_book(language: str = Query("python"), user_id: str = Query("default")):
    """获取错题本"""
    return get_error_book(language, user_id)


@router.get("/stats")
async def get_stats(language: str = Query("python"), user_id: str = Query("default")):
    """获取错题统计"""
    return get_error_stats(language, user_id)
