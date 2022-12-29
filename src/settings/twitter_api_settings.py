from pydantic import BaseSettings, Field


class TwitterSettings(BaseSettings):
    api_key = Field(env="API_KEY", default="")
    api_secret_key = Field(env="API_SECRET_KEY", default="")

    def keys(self):
        return self.api_key, self.api_secret_key
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
