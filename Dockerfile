FROM python:3.6.7-alpine3.8

WORKDIR /code

COPY ./requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

CMD ["python3", "app.py"]


