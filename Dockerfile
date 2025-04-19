# Use a specific Python version to avoid future incompatibility
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the app.py (outside the folder) into the container's /app directory
COPY ./app.py /app/app.py

# Copy templates directory (still inside the build context)
COPY ./templates /app/templates

# Copy the requirements.txt into the container
COPY ./requirements.txt /app/
COPY ./moviesss.csv /app/moviesss.csv
# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose port (ensure this is the correct port for your app)
EXPOSE 5000

# Set environment variable for Python output buffering
ENV PYTHONUNBUFFERED=1

# Start the application
CMD ["python", "/app/app.py"]
