ARG PYTHON_VERSION=3.8.1-slim

FROM python:$PYTHON_VERSION AS base

ENV PYTHON_VERSION="$PYTHON_VERSION"

FROM base AS dependencies

COPY requirements.txt .
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpython3-dev \
    && rm -rf /var/lib/apt/lists/* \
    && pip install -r requirements.txt \
    && apt-get purge -y --auto-remove gcc libpython3-dev

# RUN pip install -r requirements.txt

FROM dependencies AS run
COPY ./test-es.py ./test-es.py

ENTRYPOINT ["python", "test-es.py"]
CMD ["run"]
