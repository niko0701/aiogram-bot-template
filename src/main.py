import asyncio
import logging
import sys
from config import bot, dp
from src.database import init_database

async def on_startup():
    await init_database()

async def main():
    # dp.startup.register(on_startup)
    # dp.include_routers(
    #     router
    # )
    #
    # await dp.start_polling(bot)
    print(await bot.get_me())

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        stream=sys.stdout
    )
    asyncio.run(main())
