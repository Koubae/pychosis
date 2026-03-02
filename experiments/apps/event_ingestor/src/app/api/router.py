from fastapi import APIRouter

from src.app.api.controller.index import router as index_router


def get_router() -> APIRouter:
    router = APIRouter()
    router.include_router(index_router)
    return router
