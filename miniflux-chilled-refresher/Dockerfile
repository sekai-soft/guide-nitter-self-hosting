# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install miniflux requests

# Run nitter-auth.py when the container launches
CMD ["python", "./miniflux-chilled-refresher.py"]
