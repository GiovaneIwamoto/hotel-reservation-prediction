# Use the official Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN apt-get update && apt-get install build-essential -y
RUN pip3 install -r requirements.txt

# Copy the application code to the working directory
COPY . .

ENV S3_BUCKET_NAME=
ENV MODEL_FILE_NAME=model.tar.gz
ENV DYNAMODB_TABLE_NAME=

# Run the FastAPI application using uvicorn server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]