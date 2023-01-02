# syntax=docker/dockerfile:1
FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

WORKDIR /code
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /code/

# RUN python manage.py collectstatic --no-input
# CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]

# COPY ./entrypoint.sh /
# ENTRYPOINT [ "sh", "/entrypoint.sh" ]
