from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()

class Config(BaseSettings):
    DB_URL: str
    DB_URL_TEST: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

config = Config()