FROM python:latest
WORKDIR /app
ADD ./app /app
RUN pip install -r requirements.txt
CMD ["python3", "weather.py"]
