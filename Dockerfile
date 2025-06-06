FROM python:3.12
# https://python-poetry.org/docs#ci-recommendations
ENV POETRY_VERSION=1.8.2
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv
# Tell Poetry where to place its cache and virtual environment
ENV POETRY_CACHE_DIR=/opt/.cache
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Creating a virtual environment just for poetry and install it with pip
RUN python3 -m venv $POETRY_VENV \
	&& $POETRY_VENV/bin/pip install -U pip setuptools poetry==${POETRY_VERSION}

# Set environment variables for Node.js
ENV NODE_VERSION=20.17.0
# Install curl and Node.js
RUN apt-get update && apt-get install -y curl \
	&& curl -fsSL https://deb.nodesource.com/setup_$NODE_VERSION.x.sh | bash - \
	&& apt-get install -y nodejs \
	&& apt-get install -y npm \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*
# Verify installation
RUN node -v && npm -v
ENV PATH="${PATH}:${POETRY_VENV}/bin"

WORKDIR /app
COPY poetry.lock pyproject.toml README.md ./
# [OPTIONAL] Validate the project is properly configured
RUN poetry check
RUN poetry install
# Copy Application
COPY . /app

COPY build.sh /app/build.sh
RUN chmod +x /app/build.sh

EXPOSE 8000

CMD ["./build.sh"]



