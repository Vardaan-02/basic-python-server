# Base Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependency list
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the full app code
COPY . .

# Set environment variables (optional fallback)
ENV FLASK_APP=run.py
ENV FLASK_RUN_PORT=8000

# Expose Flask port
EXPOSE 8000

# Run the app
CMD ["python", "run.py"]
