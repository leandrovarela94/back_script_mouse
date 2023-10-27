FROM python:3.11-slim

# Define the working directory
WORKDIR /app

# Expose port
EXPOSE 8000

# Copy the project files to the working directory
COPY . /app

# Install system dependencies
RUN apt-get update && apt-get install -y libevdev-dev

# Install pipenv
RUN pip install pip --upgrade
RUN pip install pipenv

# Install project dependencies
RUN pipenv install --system --deploy

# Set the command to run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]