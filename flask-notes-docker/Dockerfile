# Use a lightweight Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app/ /app/

# Create a non-root user
RUN useradd -m flaskuser
USER flaskuser

# Expose Flask port
EXPOSE 5000

# Start Flask app
CMD ["python", "app.py"]
