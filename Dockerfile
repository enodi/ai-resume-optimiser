# Use the official Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
  build-essential \
  libmagic-dev \
  poppler-utils \
  && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

EXPOSE 7860

# Run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.address=0.0.0.0"]
