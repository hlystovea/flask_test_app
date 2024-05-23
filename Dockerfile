FROM python:3.12-slim
WORKDIR /code
COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY ./gunicorn.conf.py ./gunicorn.conf.py
COPY ./src ./src