from pydantic import BaseModel, Field
from uuid import UUID

class UserBase(BaseModel):
  name: str = Field(..., min_length=1, max_length=20, example="ブレーダー名")

class UserCreate(UserBase):
  firebase_uuid: str = Field(..., example="firebase uuid")

class User(UserBase):
  id: UUID  

class Config:
  orm_mode = True
