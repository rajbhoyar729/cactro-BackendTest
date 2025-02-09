from fastapi import HTTPException, status
from app.config import settings
from app.models.cache_item import CacheItem
from app.repositories.cache_repository import CacheRepository

class CacheService:
    def __init__(self, repository: CacheRepository = None):
        self.repository = repository or CacheRepository()

    async def create_or_update_cache(self, key: str, value: str) -> CacheItem:
        existing = await self.repository.get_by_key(key)
        if existing:
            return await self.repository.update(existing, value)
        
        count = await self.repository.count()
        if count >= settings.max_size:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Cache is full. Cannot add new item."
            )
        
        new_item = CacheItem(key=key, value=value)
        return await self.repository.create(new_item)

    async def get_cache(self, key: str) -> CacheItem:
        item = await self.repository.get_by_key(key)
        if not item:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Key not found in cache."
            )
        return item

    async def delete_cache(self, key: str) -> None:
        item = await self.repository.get_by_key(key)
        if not item:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Key not found in cache."
            )
        await self.repository.delete(item)
