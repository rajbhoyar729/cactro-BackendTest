from pydantic import Field
from beanie import Document

class CacheItem(Document):
    key: str = Field(..., example="sample_key")
    value: str = Field(..., example="sample_value")

    class Settings:
        name = "cache_collection"
        indexes = ["key"]
