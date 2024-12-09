# Use an official Python image as the base image
FROM python:3.12-slim

# Create and set the working directory
WORKDIR /app

# Install system-level dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    pkg-config \
    libcairo2-dev \
    python3-dev \
    libpango1.0-dev \
    poppler-utils \
    inkscape \
    libgtk-3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy Pipfile and Pipfile.lock
COPY Pipfile Pipfile.lock /app/

# Install code-level dependencies
RUN pip install --upgrade pip \
    && pip install pipenv \
    && pipenv install --system --deploy

# Copy the project files into the container
COPY . /app

# Define the entrypoint
CMD ["uvicorn", "src.interfaces.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
