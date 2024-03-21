FROM python:3.11.8
COPY requirements.txt .
COPY .env .
RUN pip install --upgrade pip && pip install -r requirements.txt
WORKDIR /opt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]