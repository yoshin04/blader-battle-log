import uuid
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID

from app.database import Base

class User(Base):
  __tablename__ = "users"

  id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
  firebase_uuid = Column(String(255))
  name = Column(String(20), index=True) # ブレーダー名

class Blade(Base):
  __tablename__ = "blades"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String(80), unique=True, index=True) # ブレード名
  image_url = Column(String(255), nullable=True) # 画像URL
  attack_power = Column(Integer) # 攻撃力
  defense_power = Column(Integer) # 防御力
  stamina = Column(Integer) # スタミナ
  weight = Column(Integer) # 重さ
  brand = Column(String(40)) # BX or UX
  type = Column(String(40)) # タイプ
  spin_type = Column(String(10)) # 回転方向

class Ratchet(Base):
  __tablename__ = "ratchets"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String(80), unique=True, index=True) # ラチェット名
  image_url = Column(String(255), nullable=True) # 画像URL
  attack_power = Column(Integer) # 攻撃力
  defense_power = Column(Integer) # 防御力
  stamina = Column(Integer) # スタミナ
  weight = Column(Integer) # 重さ
  height = Column(Integer) # 高さ

class Bit(Base):
  __tablename__ = "bits"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String(80), unique=True, index=True) # ビット名
  image_url = Column(String(255), nullable=True) # 画像URL
  attack_power = Column(Integer) # 攻撃力
  defense_power = Column(Integer) # 防御力
  stamina = Column(Integer) # スタミナ
  weight = Column(Integer) # 重さ
  burst_resistance = Column(Integer) # バースト耐性
