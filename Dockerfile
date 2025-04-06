FROM python:3.13

WORKDIR /online_work

COPY pyproject.toml poetry.lock ./

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-root && \
    pip install celery && \
    pip install stripe && \
    pip install django-celery-beat

COPY . .


RUN mkdir -p /app/media


EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]



