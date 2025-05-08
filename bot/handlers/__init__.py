from aiogram import Router
from .admin import router as admin

router = Router(name="Handlers")
router.include_routers(
    admin,
)

