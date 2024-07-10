from pydantic import BaseModel, Field
from typing import Optional

class RatchetBase(BaseModel):
  name: str = Field(..., min_length=1, max_length=80, example="ラチェット名")
  image_url: Optional[str] = Field(None, max_length=255, example="https://example.com/image.jpg")
  attack_power: int = Field(..., le=100, example=20)
  defense_power: int = Field(..., le=100, example=20)
  stamina: int = Field(..., le=100, example=20)
  weight: int = Field(..., le=100, example=20)
  height: int = Field(..., le=100, example=20)
