from fastapi import APIRouter
from src.constants.constants import API_PREFIX
from src.routers.mini_app_route import router as mini_app_route

routers = APIRouter()

# MiniApp
routers.include_router(
    mini_app_route, prefix=f"{API_PREFIX}/mini_app", tags=["MiniApp"])
