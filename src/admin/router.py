from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from src.admin.callbacks import AdminCallback
from src.admin.filters import AdminFilter
from .utils import logger, TEXT
from src.utils.telegram import try_edit
from .admin_manager.router import router as manager

router = Router(name="Admin Router")

router.include_routers(manager)


# Example how to use handler for both message and callback
@router.callback_query(AdminCallback.filter(F.data == "admin"))
@router.message(Command("admin"), AdminFilter())
async def admin_start(message: Message | CallbackQuery):
    logger.info(f"Admin start requested by {message.from_user.id}")
    text = TEXT["START"]
    await try_edit(message, text=text)
