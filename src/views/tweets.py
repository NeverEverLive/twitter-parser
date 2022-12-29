from fastapi import APIRouter

from src.components.tweets.methods import get_tweets
from src.components.tweets.schemas import TweetsResponseSchema


router = APIRouter(prefix="/tweets")


@router.get("/{twitter_id}", response_model=TweetsResponseSchema)
async def get_last_tweets(twitter_id: int):
    tweets = await get_tweets(twitter_id)
    return TweetsResponseSchema(data=tweets, message="Tweets get successfuly")
