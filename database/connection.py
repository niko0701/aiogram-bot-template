from tortoise import Tortoise
from config import TORTOISE_ORM


async def init_database():
    """
    Function for initializing database and creating tables mentioned in database_models
    """
    await Tortoise.init(config=TORTOISE_ORM)   
    await Tortoise.generate_schemas()
