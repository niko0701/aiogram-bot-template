from aiogram import Router
from src.admin.panel.router import router as panel
from src.admin.admin_manager.router import router as manager

router = Router(name="Admin Router")

router.include_routers(panel, manager)
