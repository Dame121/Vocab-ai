# ---------- 1. Base image ----------
# Start from a lightweight Python image
FROM python:3.11-slim

# ---------- 2. Set working directory ----------
# All subsequent commands run inside /app in the container
WORKDIR /app

# ---------- 3. Copy and install dependencies first ----------
# Copying requirements.txt separately lets Docker cache this layer.
# If your code changes but dependencies don't, Docker skips reinstalling.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---------- 4. Copy the rest of your project ----------
COPY . .

# ---------- 5. Expose the port ----------
# Tells Docker (and readers) that the app listens on port 8000
EXPOSE 8000

# ---------- 6. Start the app ----------
# Launches your FastAPI app with Uvicorn when the container starts
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]