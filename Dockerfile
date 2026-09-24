# Portfolio demo: minimal Python runtime for future agent snippets
FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Default: show portfolio help
CMD ["python", "-c", "print('technical-portfolio-showcase: import n8n-workflows/*.json into n8n')"]
