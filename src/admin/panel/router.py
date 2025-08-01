from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from src.admin.callbacks import AdminCallback
from src.admin.filters import AdminFilter
from src.admin.text import AdminText
from src.utils import try_edit


router = Router(name="Admin Start")


# Example how to use handler for both message and callback
@router.callback_query(AdminCallback.filter(F.data == "admin"))
@router.message(Command("admin"), AdminFilter())
async def admin_start(message: Message | CallbackQuery):
    text = AdminText.START
    await try_edit(message=message, text=text)
