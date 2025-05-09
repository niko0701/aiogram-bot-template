from aiogram import Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from bot.filters.admin import AdminFilter
from bot.text.admin import AdminText
from utilits.supportive_function import try_edit


router = Router(name="Admin Start")


@router.message(Command("admin"), AdminFilter())
async def admin_start(message: Message | CallbackQuery):
    text = AdminText.START
    await try_edit(message=message, text=text)
