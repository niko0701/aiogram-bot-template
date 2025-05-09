from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.types import CallbackQuery, Message

from bot.filters.admin import AdminFilter
from bot.text.admin import AdminText
from bot.text.base import BaseText
from database.models.admin import Admin
from utilits.supportive_function import try_edit


router = Router(name="Admin Start")


@router.message(Command("admin"), AdminFilter())
async def admin_start(message: Message | CallbackQuery):
    text = AdminText.START
    await try_edit(message=message, text=text)


@router.message(Command("add_admin"), AdminFilter(True))
async def add_admin(message: Message, command: CommandObject):
    tg_id = command.args
    if not tg_id.isdigit():
        await message.answer(text=BaseText.NOT_ISDIGIT)
        return
