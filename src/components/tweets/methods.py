import os

from aiohttp import ClientSession
from dotenv import load_dotenv

from src.settings.proxy_settings import ProxySettings


load_dotenv()

twitter_url = "https://api.twitter.com/2/users/{}/tweets"
params = {
    "max_results": 10
}
headers = {
    "Authorization": f"Bearer {os.getenv('API_BEARER_TOKEN')}"
}


async def get_tweets(_id: int):
    async with ClientSession(headers=headers) as session:
        async with session.get(
            twitter_url.format(_id), 
            params=params, 
            proxy=ProxySettings().get_url()
        ) as response:
            if response.status == 200:
                tweets = (await response.json())["data"]
            else:
                # TODO raise custom exception
                pass
    return tweets
