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


class ChatIdFilter(Filter):
    """
    Filter by chat id
    """
    async def __init__(self, chat_ids: list[int]):
        self.chat_ids = chat_ids

    async def __call__(self, message: Message | CallbackQuery) -> bool:
        type_of_update = type(message)
        if type_of_update == Message:
            chat_id = message.chat.id
        else:
            chat_id = message.message.chat.id
        return chat_id in self.chat_ids
