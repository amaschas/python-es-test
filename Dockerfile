ARG PYTHON_VERSION=3.8.1-slim-buster

FROM python:$PYTHON_VERSION AS base

ENV PYTHON_VERSION="$PYTHON_VERSION"

FROM base AS dependencies

COPY requirements.txt .
RUN pip install --no-cache-dir --src /src -r requirements.txt

FROM dependencies AS run
WORKDIR /app


COPY ./test-es.py ./test-es.py

ENTRYPOINT ["python", "test-es.py"]
CMD ["run"]
