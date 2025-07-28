FROM python:3.11-slim-bookworm

# Set the working directory inside the container
WORKDIR /app

# Copy the entire project context
COPY . .

# Install the Python dependencies from the correct path
RUN pip install --no-cache-dir -r src/backend/requirements.txt

# Expose the port the application will run on
EXPOSE 8080

# Run the application as a module, which is necessary for relative imports.
# The WORKDIR is automatically added to the PYTHONPATH.
CMD ["python3", "-m", "src.backend.main"]
