FROM python:3.12-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.12-slim AS final

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.12 /usr/local/lib/python3.12
COPY --from=builder /usr/local/bin /usr/local/bin

COPY src/ ./src

COPY docker/init_db.sh /app/
RUN sh /app/init_db.sh

EXPOSE 8000

ENV PYTHONPATH="/app/src"

CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000"]
