from typing import List

from pydantic import BaseModel, Field

from src.components.response import BaseResponse


class Tweet(BaseModel):
    id: str
    edit_history_tweet_ids: List[str]
    text: str

class TweetsResponseSchema(BaseResponse):
    data: List[Tweet]
