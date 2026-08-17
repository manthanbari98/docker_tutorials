# Pull base image for Python
FROM python:3.8-slim

# Set the working directory in the image
WORKDIR /app

# Copy requirements file
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents at /app in the image
COPY . /app

# Run the application
CMD ["python", "app.py"]