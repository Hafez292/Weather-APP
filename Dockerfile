FROM python:3.10-slim

#determinde the folder in the container to operate the app
WORKDIR /app

# to copy all files that related to app into previuos folder
COPY . /app

# تثبيت الباكجات المطلوبة
RUN pip install  -r requirements.txt

# فتح البورت 8000
EXPOSE 5000

# أمر التشغيل
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
