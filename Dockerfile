FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV HOME=/app
ENV STREAMLIT_HOME=/app/.streamlit
ENV HF_HOME=/app/huggingface

# Install system dependencies
RUN apt-get update && apt-get install -y \
  build-essential \
  libpoppler-cpp-dev \
  pkg-config \
  python3-dev \
  && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Create necessary directories
RUN mkdir -p /app/.streamlit /app/huggingface

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy all files
COPY . .

# Expose Streamlit port
EXPOSE 7860

# Run the app
CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.address=0.0.0.0"]
