from aiogram import Router
from .start import router as start


router = Router(name="Admin")
router.include_routers(
    start,
)
