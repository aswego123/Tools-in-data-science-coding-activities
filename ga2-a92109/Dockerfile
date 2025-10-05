# Use Python 3.11 slim image
FROM python:3.11-slim

# Create user with UID 1000 (required by Hugging Face Spaces)
RUN useradd -m -u 1000 user

# Set working directory
WORKDIR /home/user/app

# Copy and install dependencies first
COPY --chown=user requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy rest of the application
COPY --chown=user . .

# Switch to non-root user
USER user

# Set environment variables
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH \
    APP_PORT=7416

# Expose the app port
EXPOSE 7416

# Run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7416"]
