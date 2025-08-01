from tortoise import Tortoise
from src.config import config


# Paths to models
database_models = [
    "database.models.user",
    "database.models.admin",
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
            },
        }
    },
    "apps": {"models": {"models": database_models, "default_connection": "default"}},
}


async def init_database():
    """
    Function for initializing database and creating tables mentioned in database_models
    """
    await Tortoise.init(config=TORTOISE_ORM)
    await Tortoise.generate_schemas()
