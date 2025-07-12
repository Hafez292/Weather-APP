FROM python:3.10-slim

WORKDIR /WeatherApp

COPY . /WeatherApp/

RUN pip3 install -r requirments.txt


CMD ["python3","weather.py"]

