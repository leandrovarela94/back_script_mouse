FROM python:3.11-slim

# Define the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential libevdev-dev python3-dev

# Copy the project files to the working directory
COPY . /app

# Install pipenv
RUN pip install pip --upgrade
RUN pip install pipenv
RUN pip install pynput
# Install project dependencies
RUN pipenv install --system --deploy

# Expose port
EXPOSE 8281

# Set the command to run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8281"]
