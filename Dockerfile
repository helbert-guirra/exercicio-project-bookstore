FROM python:3.13-slim AS python-base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.8.4 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    PATH="/opt/poetry/bin:$PATH"

# Instalar curl + build-essential + Poetry
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        curl \
        build-essential \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && /opt/poetry/bin/poetry --version

# Instalar dependências do Postgres
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

WORKDIR /app
COPY poetry.lock pyproject.toml ./

RUN /opt/poetry/bin/poetry install --no-dev

RUN /opt/poetry/bin/poetry install

COPY . /app/

EXPOSE 8000

CMD ["/opt/poetry/bin/poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]