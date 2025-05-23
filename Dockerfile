# Dockerfile (Simple Version)

# Use the official uv base image
FROM ghcr.io/astral-sh/uv:python3.12-alpine

# Set the working directory in the container
WORKDIR /app

# Copy application code
COPY ./app /app/app
COPY ./models /app/models
COPY requirements.txt .

# Create virtual environment and install dependencies using uv
RUN uv venv /app/.venv && \
    . /app/.venv/bin/activate && \
    uv pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 8000

# Define the command to run your application when the container starts
# Activate the virtual environment and run uvicorn
CMD ["/bin/sh", "-c", ". /app/.venv/bin/activate && uvicorn app.gift_predictor:app --host 0.0.0.0 --port 8000"]
