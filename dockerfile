# Use a slim Python base image
FROM python:3.12-slim

# Install uv (fast Python dependency manager)
RUN pip install --no-cache-dir uv

WORKDIR /app

# Copy dependency files first (better caching)
COPY pyproject.toml uv.lock* ./

# Then copy only necessary source files
COPY cs599o_warmup/ ./cs599o_warmup/
COPY tests/ ./tests/
COPY README.md ./

CMD ["pytest", "-q"]

# Run tests inside uv environment by default
CMD ["uv", "run", "pytest", "-q"]