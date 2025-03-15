# Use Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Expose the port (optional if the app runs a web service)
EXPOSE 5000

# Define the command to run your application
CMD ["python", "calculator.py"]
