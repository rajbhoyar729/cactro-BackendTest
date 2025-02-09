from dotenv import load_dotenv
import os
from pydantic import BaseSettings


load_dotenv()

class Settings(BaseSettings):
    mongo_uri: str = os.getenv("MONGO_URI")
    db_name: str = os.getenv("DB_NAME", "cache_db")
    max_size: int = int(os.getenv("MAX_SIZE", "10"))

    class Config:
        env_file = ".env"

settings = Settings()
