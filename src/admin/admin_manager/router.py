from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandObject
from aiogram.types import Message

from src.admin.filters import AdminFilter
from .text import Text
from src.admin.models import Admin
from src.admin import logger


router = Router(name="Admin Manager")


@router.message(Command("add_admin"), AdminFilter(True))
async def add_admin(message: Message, command: CommandObject):
    """
    Function for adding admins (Available only for base admins whose ids are in config.ADMINS)
    """
    if not command.args:
        return
    tg_id = command.args
    admin: Admin | None = await Admin.filter(tg_id=tg_id).first()
    if admin:
        await message.answer(text=Text.ADMIN_ALREADY_EXISTS)
        return
    admin = Admin(tg_id=tg_id)
    await admin.save()
    logger.info(f"Admin added: {tg_id}")
    await message.answer(text="Admin added")


@router.message(Command("admin_list"), AdminFilter(True))
async def admin_list(message: Message):
    """
    Function for getting a list of admins
    """
    logger.info(f"Admin list requested by {message.from_user.id}")
    admins = await Admin.all()
    if len(admins) == 0:
        await message.answer(text=Text.ADMIN_LIST_EMPTY)
        return
    text = "List of added admins:\n"
    for admin in admins:
        text += f"[{admin.tg_id}](https://t.me/user?id={admin.tg_id})\n"
    await message.answer(text=text, parse_mode=ParseMode.MARKDOWN)


@router.message(Command("remove_admin"), AdminFilter(True))
async def remove_admin(message: Message, command: CommandObject):
    """
    Function for removing admins (Available only for base admins whose ids are in ADMINS env variable)
    """
    if not command.args:
        return
    tg_id = command.args
    admin: Admin | None = await Admin.filter(tg_id=tg_id).first()
    if not admin:
        await message.answer(text=Text.ADMIN_NOT_EXISTS)
        return
    await admin.delete()
    logger.info(f"Admin removed: {tg_id}")
    await message.answer(text=Text.ADMIN_REMOVED)
