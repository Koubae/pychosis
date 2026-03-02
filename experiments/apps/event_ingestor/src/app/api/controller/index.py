from fastapi import APIRouter
from fastapi.responses import JSONResponse


__all__ = ("router",)

router = APIRouter(
    tags=[
        "Index",
    ]
)


@router.get("/")
def index() -> JSONResponse:
    return JSONResponse(content={"message": "Service is running"})


@router.get("/health")
def health() -> JSONResponse:
    return JSONResponse(content={"message": "OK"})


@router.get("/ready")
def ready() -> JSONResponse:
    return JSONResponse(content={"message": "OK"})
