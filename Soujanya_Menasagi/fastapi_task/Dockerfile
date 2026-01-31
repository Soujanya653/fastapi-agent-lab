# 1. Base image (Python)
FROM python:3.10-slim

# 2. Set working directory inside container
WORKDIR /app

# 3. Copy dependency file
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy application files
COPY main.py .
COPY agent.py .
COPY schemas.py .

# 6. Expose FastAPI port
EXPOSE 8000

# 7. Start FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
