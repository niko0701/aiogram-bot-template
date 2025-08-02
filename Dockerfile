# Use official Python 3.11 slim image as base
FROM python:3.11-slim

# Set working directory to /app
WORKDIR /app

# Copy dependency files first (for better layer caching)
COPY pyproject.toml poetry.lock /app/

# Install Poetry (package manager)
RUN pip install poetry

# Install project dependencies (without the root package) and clean cache
RUN poetry install --no-root && rm -rf $POETRY_CACHE_DIR

# Copy all remaining source files
COPY . /app/

# Run the application using Poetry's environment
# Using module syntax (-m) for proper package imports
CMD ["poetry", "run", "python", "-m", "src.main"]
