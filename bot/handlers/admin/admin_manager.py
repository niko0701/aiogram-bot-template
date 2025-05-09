from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message

from bot.filters.admin import AdminFilter
from bot.text.admin import AdminText
from bot.text.base import BaseText
from database.models.admin import Admin


router = Router(name="Admin Manager")


@router.message(Command("add_admin"), AdminFilter(True))
async def add_admin(message: Message, command: CommandObject):
    """
    Function for adding admins (Available only for base admins whose ids are in config.ADMINS)
    """
    tg_id: str = command.args
    if not tg_id.isdigit():
        await message.answer(text=BaseText.NOT_ISDIGIT)
        return
    tg_id: int = int(tg_id)
    admin: Admin | None = await Admin.filter(tg_id=tg_id).first()
    if admin:
        await message.answer(text=AdminText.ADMIN_ALREADY_EXISTS)
        return
    admin = Admin(tg_id=tg_id)
    await admin.save()
    await message.answer(text="Admin added")



@router.message(Command("admin_list"), AdminFilter(True))
async def admin_list(message: Message):
    admins = await Admin.all()
    if len(admins) == 0:
        await message.answer(text=AdminText.ADMIN_LIST_EMPTY)
        return
    text = "List of added admins:\n"
    for admin in admins:
        text += f"[{admin.tg_id}](https://t.me/user?id={admin.tg_id})\n"
    await message.answer(text=text)


@router.message(Command("remove_admin"), AdminFilter(True))
async def remove_admin(message: Message, command: CommandObject):
    """
    Function for removing admins (Available only for base admins whose ids are in config.ADMINS)
    """
    tg_id: str = command.args
    if not tg_id.isdigit():
        await message.answer(text=BaseText.NOT_ISDIGIT)
        return
    tg_id: int = int(tg_id)
    admin: Admin | None = await Admin.filter(tg_id=tg_id).first()
    if not admin:
        await message.answer(text=AdminText.ADMIN_NOT_EXISTS)
        return
    await admin.delete()
    await message.answer(text=AdminText.ADMIN_REMOVED)

