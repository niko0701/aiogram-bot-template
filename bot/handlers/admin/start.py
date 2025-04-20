from aiogram import Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from bot.filters.admin import AdminFilter


router = Router(name="Admin Start")


@router.message(Command("admin"), AdminFilter())
async def admin_start(message: Message | CallbackQuery):
    pass
