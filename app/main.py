from fastapi import FastAPI
from app.core.database import init_db
from app.routes import cache

app = FastAPI(title="Customizable Caching API with dotenv")

@app.on_event("startup")
async def startup_event():
    await init_db()

app.include_router(cache.router)
