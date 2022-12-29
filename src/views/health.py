from fastapi import APIRouter

from src.components.response import BaseResponse

router = APIRouter()


@router.get("", response_model=BaseResponse, status_code=200)
def health_endpoint():
    return BaseResponse(message="It's OK!")
