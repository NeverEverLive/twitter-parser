from pydantic import BaseModel, Field


class BaseResponse(BaseModel):
    message: str
    success: bool = Field(default=True)