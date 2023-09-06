FROM python:3.10.12

COPY requirements.txt /app/requirements.txt

RUN cd /app && pip install -r requirements.txt

ADD . /app

WORKDIR /app

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]