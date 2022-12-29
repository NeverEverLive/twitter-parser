from pydantic import BaseSettings, Field


class ProxySettings(BaseSettings):
    username = Field(env="PROXY_USERNAME",default="")
    password = Field(env="PROXY_PASSWORD",default="")
    ip = Field(env="PROXY_IP",default="localhost")
    port = Field(env="PROXY_PORT",default="443")

    def get_url(self):
        return f"http://{self.username}:{self.password}@{self.ip}:{self.port}"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
