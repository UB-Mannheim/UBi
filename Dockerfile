FROM docker.io/library/python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY ./code /app

RUN pip install --root-user-action ignore --upgrade pip && \
    pip install --root-user-action ignore -r requirements.txt && \
    rm -rf /root/.cache

EXPOSE 8000

CMD ["chainlit", "run", "app.py", "--host", "0.0.0.0", "-w"]
