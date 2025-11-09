# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies (in case any Python libs need them)
# Note: mysql-connector-python often needs gcc/build-essential
# but we'll try without first. Let's add them to be safe.
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the dependencies file
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
# Using --no-cache-dir reduces image size
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the backend application code
COPY ./app /app/app

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run uvicorn when the container launches
# --host 0.0.0.0 is critical to allow connections from outside the container
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]