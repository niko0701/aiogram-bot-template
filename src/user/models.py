from src.models import Base
from tortoise import fields


class User(Base):
    """
    Basic model for storing most common data about telegram users
    """
    tg_id = fields.BigIntField()  # Telegram user id
    username = fields.CharField(
        max_length=100, null=True
    )  # Username from telegram, can be null
    full_name = fields.CharField(max_length=100)  # First name and last name together
