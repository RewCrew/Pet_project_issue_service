FROM python:3.7-slim

WORKDIR /app


RUN pip install --upgrade pip

COPY ./setup.cfg .
COPY ./setup.py .

RUN pip install --no-cache-dir --upgrade -e '.[dev]'


COPY . ./issues_service

CMD [ "python", "issues_service/run.py" ]