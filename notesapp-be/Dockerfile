# --- Base Stage: Build dependencies ---
FROM python:3.10-slim AS builder

WORKDIR /app

# Install dependencies in a separate layer for caching
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


# --- Final Stage: Application runtime ---
FROM python:3.10-slim

WORKDIR /app

# Copy installed dependencies from builder stage to keep the final image lightweight
COPY --from=builder /install /usr/local

# Copy application code
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Expose application port
EXPOSE 8000

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "notesapp.wsgi"]
