FROM python:3.9
EXPOSE 8000
WORKDIR /django_template

ENV PYTHONUNBUFFERED 1

COPY . /django_template/

RUN pip3 install poetry

RUN poetry export --without-hashes -f requirements.txt --output requirements.txt
RUN pip3 install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
