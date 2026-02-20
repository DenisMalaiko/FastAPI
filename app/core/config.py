from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Config(BaseSettings):
    DB_URL: str

    class Config:
        env_file = ".env"

config = Config()