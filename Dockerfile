FROM python:3.6.7-alpine3.8

WORKDIR /code

COPY ./requirements.txt /requirements.txt
RUN pip3 install -i https://mirrors.aliyun.com/pypi/simple/ -r /requirements.txt

CMD ["gunicorn", "wsgi", "--bind", "0.0.0.0:5000"]


