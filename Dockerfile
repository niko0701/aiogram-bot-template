from python:3.11-slim

workdir /app

copy pyproject.toml poetry.lock /app/

run pip install poetry

run poetry install --no-root && rm -rf $POETRY_CACHE_DIR

copy . /app/

CMD ["poetry", "run", "python", "-m", "src.main"]
