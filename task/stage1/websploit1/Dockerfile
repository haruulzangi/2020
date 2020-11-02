FROM python:3-alpine

WORKDIR /app/

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY chall.py /app/
COPY flag.txt /app/

ENV WERKZEUG_DEBUG_PIN=off

ENTRYPOINT ["python", "chall.py"]
