FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1
ENV  PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /app

COPY . /app

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]


