FROM python:3.10-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Copy requirements.txt first (better for Docker caching)
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy all your application files
COPY . .

EXPOSE 8888

# Run your application 
CMD ["python", "run.py"]
