from pydantic import BaseModel, Field
from typing import Optional

class BladeBase(BaseModel):
  name: str = Field(..., min_length=1, ma_length=80, example="ブレード名")
  image_url: Optional[str] = Field(None, max_length=255, example="https://example.com/image.jpg")
  attack_power: int = Field(..., le=100, example=20)
  defense_power: int = Field(..., le=100, example=20)
  stamina: int = Field(..., le=100, example=20)
  weight: int = Field(..., le=100, example=20)
  brand: str = Field(..., max_length=40, example="BX")
  type: str = Field(..., max_length=40, example="アタック")
  spin_type: str = Field(..., max_length=10, example="right")

class BladeCreate(BladeBase):
  pass

class Blade(BladeBase):
  id:int
  
class Config:
  orm_mode = True
