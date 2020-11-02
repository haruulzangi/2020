FROM python:3-alpine

WORKDIR /app/

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY chall.py /app/
COPY flag.txt /app/

ENTRYPOINT ["python", "chall.py"]
