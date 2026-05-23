FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY app.py .

RUN useradd --system --uid 10001 backend2 && \
    chown -R backend2:backend2 /app

USER backend2

EXPOSE 5001

CMD ["python", "app.py"]
