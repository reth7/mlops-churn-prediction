# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirement files
COPY requirements.txt .

# Install Python dependencies
RUN pip install --default-timeout=100 --retries=10 --no-cache-dir -r requirements.txt

# Copy entire app
COPY . .

# Expose API port
EXPOSE 8000

# Run FastAPI with Uvicorn
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
