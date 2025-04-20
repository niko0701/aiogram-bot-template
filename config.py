from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv
from os import getenv
from aiogram import Bot, Dispatcher


class Config:
    load_dotenv()

    # Telegram Bot Token
    BOT_TOKEN: str = str(getenv('BOT_TOKEN'))
    # Telegram ids of admins as string, need for validation and access to admin functions
    ADMINS: str = str(getenv('ADMINS'))    

    # Database data for postgres
    POSTGRES_HOST: str = str(getenv("POSTGRES_HOST"))
    POSTGRES_PORT: int = int(str(getenv("POSTGRES_PORT")))
    POSTGRES_DB: str = str(getenv("POSTGRES_DB"))
    POSTGRES_USER: str = str(getenv("POSTGRES_USER"))
    POSTGRES_PASSWORD: str = str(getenv("POSTGRES_PASSWORD"))


config = Config()


bot = Bot(
    token=config.BOT_TOKEN, 
    default=DefaultBotProperties(parse_mode=ParseMode.HTML, link_preview_is_disabled=True)
)

dp = Dispatcher()

database_models = [
    "database.models.user",
]

TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "database": config.POSTGRES_DB,
                "host": config.POSTGRES_HOST,
                "password": config.POSTGRES_PASSWORD,
                "port": config.POSTGRES_PORT,
                "user": config.POSTGRES_USER,
            }
        }
    },
    "apps": {
        "models": {
            "models": database_models,
            "default_connection": "default"
        }
    }
}
