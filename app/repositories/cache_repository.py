from typing import Optional
from app.models.cache_item import CacheItem

class CacheRepository:
    async def get_by_key(self, key: str) -> Optional[CacheItem]:
        return await CacheItem.find_one(CacheItem.key == key)

    async def create(self, cache_item: CacheItem) -> CacheItem:
        await cache_item.create()
        return cache_item

    async def update(self, cache_item: CacheItem, value: str) -> CacheItem:
        cache_item.value = value
        await cache_item.save()
        return cache_item

    async def delete(self, cache_item: CacheItem) -> None:
        await cache_item.delete()

    async def count(self) -> int:
        return await CacheItem.find_all().count()
