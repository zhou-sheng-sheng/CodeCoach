"""
数据看板 API
"""

from fastapi import APIRouter, Query
import api.assessment as assessment_mod
from services.dashboard_service import get_dashboard_data

router = APIRouter(prefix="/api/dashboard", tags=["dashboard"])


@router.get("")
async def dashboard(language: str = Query("python"), user_id: str = Query("default")):
    return get_dashboard_data(
        language,
        assessment_mod._last_results.get(user_id, {}).get(language),
        user_id,
    )
