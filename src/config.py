from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv
from os import getenv
from aiogram import Bot, Dispatcher
from pydantic_settings import BaseSettings, SettingsConfigDict
import pathlib

BASE_DIR = pathlib.Path(__file__).parent.parent.parent.resolve()


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env", env_file_encoding="utf-8", extra="ignore"
    )
    # Telegram Bot Token
    BOT_TOKEN: str = str(getenv("BOT_TOKEN"))
    # Telegram ids of admins as string, need for validation and access to admin functions
    ADMINS: str = str(getenv("ADMINS"))

    # Database data for postgres
    POSTGRES_HOST: str = str(getenv("POSTGRES_HOST"))
    POSTGRES_PORT: int = int(str(getenv("POSTGRES_PORT")))
    POSTGRES_DB: str = str(getenv("POSTGRES_DB"))
    POSTGRES_USER: str = str(getenv("POSTGRES_USER"))
    POSTGRES_PASSWORD: str = str(getenv("POSTGRES_PASSWORD"))


config = Config()


bot = Bot(
    token=config.BOT_TOKEN,
    default=DefaultBotProperties(
        parse_mode=ParseMode.MARKDOWN, link_preview_is_disabled=True
    ),
)

dp = Dispatcher()
