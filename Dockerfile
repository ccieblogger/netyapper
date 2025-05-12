# syntax=docker/dockerfile:1
FROM python:3.10-alpine

WORKDIR /app

# Install build dependencies for Poetry and psycopg2
RUN apk add --no-cache gcc musl-dev postgresql-dev libffi-dev

# Install Poetry
RUN pip install poetry

# Copy project files
COPY pyproject.toml ./
COPY app ./app
COPY core ./core
COPY schemas ./schemas
COPY mcp_clients ./mcp_clients
COPY cli ./cli

# Install dependencies
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
