# Modular Telegram Bot Template

This is a modular Telegram bot template built with Python, using the Aiogram framework, PostgreSQL, and Docker for deployment. The project follows a modular architecture, separating concerns into distinct modules for scalability and maintainability.

## Overview
- **Modular Design**: The codebase is organized into modules (`admin`, `user`, `utils`) with dedicated sub-packages for functionality like logging, database handling, and admin features.
- **Dependencies**: Managed via [Poetry](https://python-poetry.org/) (`pyproject.toml`, `poetry.lock`).
- **Containerization**: Uses `docker-compose.yml` and `Dockerfile` for easy deployment.
- **Logging**: Module-specific logging with colored console output and file storage (`utils/logger.py`).
- **Formatting**: Consistent code formatting with [Ruff](https://github.com/astral-sh/ruff).
- **ORM**: [Tortoise ORM](https://tortoise.github.io/) for database interactions (`models.py`).

## Structure
```
.
├── docker-compose.yml # Defines services (bot, PostgreSQL) and networking.
├── Dockerfile
├── .env.sample # Sample environment variables for configuration.
├── logs
├── poetry.lock
├── pyproject.toml
├── README.md
├── requirements.txt
└── src # Core application code.
    ├── admin # Admin-specific features (e.g., `admin_manager`, `keyboards`, `router`) 
    │   ├── admin_manager
    │   │   ├── __init__.py
    │   │   ├── keyboards.py
    │   │   └── router.py
    │   ├── text.py
    │   └── callbacks.py
    ├── filters.py
    ├── __init__.py
    ├── models.py
    ├── router.py
    ├── states.py
    ├── text.py
    ├── config.py
    ├── database.py
    ├── filters.py
    ├── main.py # Entry point for the bot.
    ├── models.py # Base model with Tortoise ORM for database interactions.
    ├── text.py
    ├── user # User-related functionality.
    │   ├── __init__.py
    │   └── models.py
    └── utils # Utility functions (e.g., `logger`, `telegram`)
        ├── __init__.py
        ├── logger.py
        └── telegram.py
```
## Setup
1. Download repository and prepare it for usage:
```bash
git clone https://github.com/niko0701/aiogram-bot-template.git # Clone the repository
rm -rf aiogram-bot-template/.git # Remove the .git directory
```
2. Install dependencies via poetry: 
```bash
poetry install --no-root
```
or 
```bash
pip install -r requirements.txt
```
3. Copy `.env.sample` to `.env` and update with your `BOT_TOKEN`, `ADMINS`, and PostgreSQL credentials.
4. Build and run with Docker:
```bash
docker-compose up --build
```

## Good Luck

⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢰⣄⠀⠙⠻⣿⠿⠟⠛⠛⠛⠿⠿⠿⣿⡿⠋⠁⠀⣠⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠅⢸⣿⣷⠀⠀⠀⠁⠒⢂⣀⣱⣿⡿⠋⠀⠀⠀⢠⣾⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⡽⡿⠋⠀⠀⠀⠀⣰⡿⡛⣿⣿⣿⠀⣀⠀⠀⠀⢹⣿⠃⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⣿⠄⣴⠖⢤⡾⠫⠞⠀⣿⣿⡇⠀⠜⢿⡄⠀⣾⡏⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠛⠀⠀⡀⠀⢁⠾⠁⢠⠎⣠⡤⠀⣰⢿⡿⠁⣠⠈⠊⠉⢴⠘⠇⠀⠀⠀⢆⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⢠⡿⠀⠀⣠⣤⣧⣼⣿⣧⣴⣿⣾⣶⣾⣿⣷⣤⣈⣤⡑⠀⠿⠏⡀⠀⠀⠀⠙⠿⢿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣷⣦⣤⡄⠤⢄⢸⡇⠀⡸⢟⣋⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣷⡐⠖⠀⠑⢀⠀⠀⣀⣀⣴⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⡰⡀⣼⠇⢁⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣌⠁⠀⠀⠀⠈⠁⢃⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡟⠠⢡⡇⣿⠀⣾⣿⡿⠋⠉⣉⠛⢿⣿⣿⣿⣿⣿⡟⠉⠉⠙⢿⣿⣷⡀⠀⢠⠰⣆⠊⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡏⢙⡿⡇⡀⢾⠀⣿⠀⣿⠃⣴⢟⣉⣉⠀⢾⣿⣿⣿⣿⣿⠆⠛⠏⠻⢦⡈⠻⣇⢸⢸⠀⢹⡆⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡄⢟⣂⣇⢈⠘⠀⢻⠸⠃⢸⠃⠚⠹⠍⡑⢸⣿⣿⣿⣿⣿⠀⢫⣭⠙⠈⢳⠀⣿⢸⢸⠀⢸⡇⣿⣿⡟⠉⠉⡉⠉⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡸⡆⡁⢸⡀⠀⢸⣆⠓⠦⠴⢗⣾⣯⣽⣛⣻⣿⡈⠢⠶⠖⢁⣿⠀⠘⠸⠐⢢⠸⢹⣿⣿⣿⣦⡀⠁⢰⣿⣿
⣿⣿⣿⡿⢀⡛⢿⣿⣿⡇⠃⡛⠜⣧⠻⣿⣿⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣶⣤⣽⣶⣿⣾⠃⢠⢠⠸⠀⣸⣿⣿⣿⣿⣿⣷⣿⣿⣿
⣿⣿⣿⣇⢀⣠⣾⣿⣿⡿⠀⠈⠢⢹⢀⢹⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⠃⡀⣜⠠⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⡰⡀⢀⣤⠈⠁⠙⣿⣿⣿⣿⣿⣿⡇⠈⣿⣿⣿⣿⣿⣿⡿⠃⠈⠀⡏⠠⢄⢠⠙⣿⣿⣿⣿⡏⢵⡘⣿⣿
⣿⣿⣿⣿⣿⣿⡯⢡⡎⠀⣵⠁⠸⡏⡆⡀⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠁⠀⠀⡀⢸⣿⠀⠀⠀⡆⠈⢿⣿⣿⣷⣭⣴⣿⣿
⣿⣿⣿⣿⣿⡿⠁⡿⠀⣸⠋⡇⣄⠃⣧⢹⣿⣶⣶⣦⣤⠀⠀⠉⠉⠁⠀⢠⣤⣤⣶⣾⣿⡇⣿⢻⠀⣄⠀⡇⣧⠈⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡇⢰⢃⣇⠏⠀⠇⢿⡈⣿⡞⠟⠛⠛⠿⠿⢸⣶⣤⣤⣤⣤⠚⠛⠙⢿⣿⡿⢰⡿⠀⡆⠿⣆⢣⣿⢰⢸⣿⣿⣿⣿⢙⢿
⣿⠿⠿⣿⣿⡇⡏⢨⣶⣶⣒⣛⣂⠁⢻⡇⢦⣀⠀⢠⣄⣚⠻⠟⡛⣛⣉⣀⣀⠀⢀⣉⡁⣿⡇⢀⢠⣤⣤⣭⣉⡛⠇⣿⣿⣿⣿⣿⣾
⣡⡎⣰⣿⣿⣷⣇⢄⠻⣿⣿⠿⢟⣧⠈⣷⠸⣿⣿⣷⣤⣒⢭⣭⣭⣭⡭⢅⣶⣿⣿⡟⢸⣿⠰⠈⣠⣲⣤⣾⠟⡡⠁⢿⣿⣿⡟⣿⣿
⣿⡄⣿⣿⣿⣿⡇⠈⠂⢹⣶⣿⡿⢡⡀⠹⡀⢻⣿⣿⣿⡿⠿⣛⣭⣵⣾⣿⣿⣿⣿⠁⣿⡏⠠⠁⠝⣿⣿⣿⡎⠁⠀⢿⣿⡏⣴⣿⣿
⣿⢇⣼⣿⣿⡇⡇⠀⠀⢾⣿⣿⡇⣣⢿⡀⡇⡜⣿⣯⣻⠿⠿⠿⣿⣿⣿⣿⣿⣿⠇⢠⡟⠀⢰⣼⣧⣈⣿⡿⡰⠀⠀⢸⣿⡇⣿⣿⣿
⣟⣿⣿⣿⣿⡇⠇⣇⠀⠈⠙⢿⣿⠏⣾⣧⠀⡇⣿⣿⣿⣿⣿⣿⣽⣿⣿⡿⣿⡿⠘⠨⢠⣮⠀⠋⣿⠿⢛⡕⠁⣠⠀⢻⣿⡇⣸⣿⣿
⣾⣿⣿⣿⣿⡇⠀⠃⣴⡄⠀⠘⠏⣸⣿⣿⢰⣷⢹⣿⣿⣿⣿⣿⣻⣿⣿⣦⣀⠀⣀⡤⣸⣿⡇⠰⢣⠀⠁⡀⠀⡿⠀⣿⣿⡇⣿⣿⣿
⣿⣿⣿⣿⣿⡇⡇⣰⣿⣷⡄⠈⠂⢿⣿⠟⣸⡇⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢹⡇⣿⣿⣿⠐⢁⣀⣼⣧⠘⡇⣇⣿⡿⢸⣿⣿⣿
