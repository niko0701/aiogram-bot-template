from python:3.11-slim

workdir /app

copy pyproject.toml poetry.lock /app/

run pip install poetry

RUN poetry install --no-root && rm -rf $POETRY_CACHE_DIR

copy . /app/

cmd ["poetry", "run", "uvicorn", "main.py"]
