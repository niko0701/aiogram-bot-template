import asyncio
import logging
from .config import bot, dp
from src.database import init_database
from src.admin.router import router as admin
from src.utils.logger import setup_root_logger, setup_logger

# Create main logger
main_logger = setup_logger("main")


async def on_startup():
    main_logger.info("Starting bot...")
    await init_database()
    main_logger.info("Bot ready to work")


async def on_shutdown():
    main_logger.info("Shutting down bot...")


async def main():
    # Setup root logging
    setup_root_logger(logging.WARNING)

    main_logger.info("Configuring bot...")

    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    dp.include_routers(admin)

    try:
        bot_info = await bot.get_me()
        main_logger.info(f"Bot started: @{bot_info.username}")

        await dp.start_polling(bot)
    except Exception as e:
        main_logger.critical(f"Critical error: {e}")
        raise
    finally:
        main_logger.info("Bot stopped")


if __name__ == "__main__":
    asyncio.run(main())
