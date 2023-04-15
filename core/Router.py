from fastapi import APIRouter

from api.api import api_router

router = APIRouter()

router.include_router(api_router)