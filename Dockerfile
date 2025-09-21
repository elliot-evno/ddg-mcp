FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PORT=8080

WORKDIR /app
COPY . .

# Install dependencies
RUN pip install -r requirements.txt && pip install .

# Expose port
EXPOSE 8080

# Start the server
CMD ["sh", "-c", "ddg_mcp-mcp --transport streamable-http --host 0.0.0.0 --port ${PORT}"]
