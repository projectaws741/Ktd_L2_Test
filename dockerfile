# Use Python 3.9 slim base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies for Oracle Instant Client
RUN apt-get update && apt-get install -y \
    libaio1 wget unzip \
    && rm -rf /var/lib/apt/lists/*

# Download & install Oracle Instant Client (Basic Lite)
RUN wget https://download.oracle.com/otn_software/linux/instantclient/instantclient-basiclite-linux.x64-21.13.0.0.0dbru.zip -O /tmp/instantclient.zip \
    && unzip /tmp/instantclient.zip -d /opt/oracle \
    && rm /tmp/instantclient.zip \
    && ln -s /opt/oracle/instantclient_21_13 /opt/oracle/instantclient \
    && echo /opt/oracle/instantclient > /etc/ld.so.conf.d/oracle-instantclient.conf \
    && ldconfig

# Set environment variables for Oracle Client
ENV LD_LIBRARY_PATH=/opt/oracle/instantclient
ENV PATH=$PATH:/opt/oracle/instantclient

# Copy requirements first for caching
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code (adjust path if app.py is in src/)
COPY src/ /app/

# Use ENTRYPOINT to always run app.py with python3
ENTRYPOINT ["python3", "app.py"]
