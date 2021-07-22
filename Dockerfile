FROM python:3.9.6
WORKDIR /app
COPY app.py /app/app.py
COPY requirements.txt /app/requirements.txt
COPY http_response.txt /app/http_response.txt
RUN pip install -r /app/requirements.txt
CMD ["python3", "/app/app.py"]
EXPOSE 61337