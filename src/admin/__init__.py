from aiogram import Router
from src.utils.logger import setup_logger
from .router import router as admin


logger = setup_logger("admin")


router = Router(name="Admin Router")

router.include_routers(admin)
