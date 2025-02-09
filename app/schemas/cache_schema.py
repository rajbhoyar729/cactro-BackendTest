from pydantic import BaseModel, Field

class CacheItemSchema(BaseModel):
    key: str = Field(..., example="sample_key")
    value: str = Field(..., example="sample_value")

    class Config:
        orm_mode = True
