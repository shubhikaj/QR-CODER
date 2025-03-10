# Dockerfile for running the fasta-api backend
FROM python:3.12-bullseye

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .
# Install the dependencies needed to run the backend
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend files
COPY . .

# Expose the port the backend will run on (8000)
EXPOSE 8000

# Start the backend
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]