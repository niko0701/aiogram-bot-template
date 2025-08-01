"""
Model for storing admins
"""
from src.models import Base
from tortoise import fields


class Admin(Base):
    tg_id = fields.BigIntField() # Telegram user id

