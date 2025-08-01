from aiogram import Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from src.admin.filters import AdminFilter
from src.admin.text import AdminText
from src.utils.telegram_message import try_edit


router = Router(name="Admin Start")


@router.message(Command("admin"), AdminFilter())
async def admin_start(message: Message | CallbackQuery):
    text = AdminText.START
    await try_edit(message=message, text=text)
