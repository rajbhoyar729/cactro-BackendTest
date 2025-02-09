from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.models.cache_item import CacheItem
from app.config import settings

async def init_db():
    client = AsyncIOMotorClient(settings.mongo_uri)
    db = client[settings.db_name]
    await init_beanie(database=db, document_models=[CacheItem])
