FROM python:3.9-slim
WORKDIR /app
ENV FLASK_APP=server.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY server.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["python", "server.py"]
