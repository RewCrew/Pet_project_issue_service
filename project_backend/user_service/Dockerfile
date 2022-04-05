FROM python:3.7-slim

WORKDIR /app


RUN pip install --upgrade pip

COPY ./setup.cfg .
COPY ./setup.py .

RUN pip install --no-cache-dir --upgrade -e '.[dev]'


COPY . ./user_service

CMD [ "python", "user_service/run.py" ]