# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables for Django
ENV PYTHONUNBUFFERED 1

# Expose the port the app will run on
EXPOSE 8000

# Run migrations and start the server when the container starts
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "notesapp.wsgi"]
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
