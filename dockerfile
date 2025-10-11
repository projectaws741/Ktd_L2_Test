FROM python:3.10-slim

RUN apt-get update && apt-get install -y libaio1 unzip wget && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN wget https://download.oracle.com/otn_software/linux/instantclient/instantclient-basiclite-linux.x64-21.13.0.0.0dbru.zip && \
    unzip instantclient-basiclite-linux.x64-21.13.0.0.0dbru.zip -d /opt/oracle && \
    rm instantclient-basiclite-linux.x64-21.13.0.0.0dbru.zip && \
    echo "/opt/oracle/instantclient_21_13" > /etc/ld.so.conf.d/oracle-instantclient.conf && ldconfig

COPY app.py /app/app.py
COPY .env /app/.env

RUN pip install cx_Oracle pandas python-dotenv

ENV LD_LIBRARY_PATH=/opt/oracle/instantclient_21_13

CMD ["python", "app.py"]
