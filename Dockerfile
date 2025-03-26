# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 
ENV DJANGO_SETTINGS_MODULE=swayna.settings 

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Create a non-root user for security
RUN addgroup --system appgroup && adduser --system --group appuser

# Ensure proper ownership of the working directory
RUN chown -R appuser:appgroup /app

# Collect static files (run as root, then fix permissions)
RUN python manage.py collectstatic --noinput
RUN chown -R appuser:appgroup /app/staticfiles

# Switch to the non-root user
USER appuser

# Expose the port that Django runs on
EXPOSE 8000

# Run Gunicorn with optimizations
CMD ["gunicorn", "--workers=4", "--threads=2", "--timeout=120", "--bind", "0.0.0.0:8000", "swayna.wsgi:application"]
