FROM python:3.9-slim
WORKDIR /app
ENV FLASK_APP=server.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY server.py .
RUN pip install flask requests
EXPOSE 5000
COPY . .
CMD ["flask", "run", "--debug"]
