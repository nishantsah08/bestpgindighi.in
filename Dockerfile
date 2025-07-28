FROM python:3.11-slim-bookworm

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r src/backend/requirements.txt

EXPOSE 8080

CMD ["python3", "-m", "src.backend.main"]