"""
Model for storing admins
"""
from database.models.base import Base
from tortoise import fields


class Admin(Base):
    tg_id = fields.BigIntField() # Telegram user id
    
