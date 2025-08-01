from aiogram.enums import ChatType
from aiogram.filters import Filter
from aiogram.types import CallbackQuery, Message

class ChatTypeFilter(Filter):
    """
    Filter for checking chat type
    """
    async def __init__(self, allowed_types: list[ChatType]):
        self.allowed_types = allowed_types
    async def __call__(self, message: Message | CallbackQuery) -> bool:
        type_of_update = type(message)
        if type_of_update == Message:
            chat_type = message.chat.type
        else:
            chat_type = message.message.chat.type
        return chat_type in self.allowed_types

