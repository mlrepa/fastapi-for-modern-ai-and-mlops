# Dockerfile (Simple Version)

# Use an official lightweight Python image as a base
# python:3.11-slim-bullseye is a good choice for a balance of size and compatibility
FROM python:3.11-slim-bullseye

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the working directory
COPY requirements.txt .

# Install Python dependencies
# --no-cache-dir reduces image size by not storing the pip cache
# --upgrade pip ensures we have a recent version of pip
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container
# Be specific about what you copy to avoid including unnecessary files
COPY ./app /app/app
COPY ./models /app/models
# If you have other directories like 'static' or 'templates', copy them too:
# COPY ./static /app/static

# Expose the port the app runs on
EXPOSE 8000

# Define the command to run your application when the container starts
# This runs Uvicorn, telling it to serve the 'app' instance
# from the 'app.gift_predictor' module.
# --host 0.0.0.0 makes it accessible from outside the container.
CMD ["uvicorn", "app.gift_predictor:app", "--host", "0.0.0.0", "--port", "8000"]
