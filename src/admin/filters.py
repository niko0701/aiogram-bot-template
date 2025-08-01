from aiogram.enums import ChatType
from aiogram.filters import Filter
from aiogram.types import Message
from src.admin.models import Admin
from src.config import config


class AdminFilter(Filter):
    """
    Filter made to restrict other users from using admin commands
    """

    def __init__(self, base_admins_only: bool = False):
        self.base_admins_only = base_admins_only

    async def __call__(self, message: Message) -> bool:
        if message.chat.type != ChatType.PRIVATE:
            return False
        if self.base_admins_only:
            return str(message.from_user.id) in config.ADMINS
        return (
            await Admin.filter(tg_id=message.from_user.id).exists()
            or str(message.from_user.id) in config.ADMINS
        )
