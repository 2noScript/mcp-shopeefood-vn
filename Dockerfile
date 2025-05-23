FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    libgtk-3-0 \
    libx11-xcb1 \
    libasound2 \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN pip install uv

WORKDIR /app

COPY requirements.txt /app/
RUN uv venv && \
    uv pip install -r requirements.txt && \
    uv run -m camoufox fetch

COPY src/ /app/src/

EXPOSE 8000

CMD ["uv", "run", "-m", "src.run"]

