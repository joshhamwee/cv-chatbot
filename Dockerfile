# Use the official Python image from the Docker Hub
FROM python:3.10-buster

# Set the working directory to /app
WORKDIR /code

# Copy the requirements.txt file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /code/

# Make port 80 available to the world outside this container
EXPOSE 80

# Run the command to start Uvicorn
CMD ["gunicorn", "main:app"]