from fastapi import APIRouter, Depends
from app.services.cache_service import CacheService
from app.schemas.cache_schema import CacheItemSchema

router = APIRouter()

def get_cache_service() -> CacheService:
    return CacheService()

@router.post("/cache", status_code=201)
async def create_cache_item(
    item: CacheItemSchema,
    service: CacheService = Depends(get_cache_service)
):
    created_item = await service.create_or_update_cache(key=item.key, value=item.value)
    return {
        "message": "Cache item created/updated successfully",
        "key": created_item.key,
        "value": created_item.value
    }

@router.get("/cache/{key}")
async def get_cache_item(key: str, service: CacheService = Depends(get_cache_service)):
    item = await service.get_cache(key)
    return {"key": item.key, "value": item.value}

@router.delete("/cache/{key}")
async def delete_cache_item(key: str, service: CacheService = Depends(get_cache_service)):
    await service.delete_cache(key)
    return {"message": "Cache item deleted successfully", "key": key}
