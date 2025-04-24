# Use the official Python image
FROM python:3.12

# Set the working directory inside the container
WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir flask

# Copy the rest of the application code into the container
COPY . .

# Expose the Flask port (adjust based on your app's config)
EXPOSE 7000

# Set environment variables (optional)
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production

# Start the Flask app using a shell (allows subprocesses to inherit environment)
CMD ["sh", "-c", "flask run --host=0.0.0.0 --port=7000"]