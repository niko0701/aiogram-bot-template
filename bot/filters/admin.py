from aiogram.enums import ChatType
from aiogram.filters import Filter
from aiogram.types import CallbackQuery, Message
from config import config

class AdminFilter(Filter):
    """
    Filter made to restrict other users from using admin commands
    """
    async def __call__(self, message: Message) -> bool:
        if message.chat.type != ChatType.PRIVATE:
            return False
        return str(message.from_user.id) in config.ADMINS
