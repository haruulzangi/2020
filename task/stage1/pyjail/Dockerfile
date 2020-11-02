FROM python:2
WORKDIR /app/
COPY flag.txt /app/
COPY jail.py /app/

ENV WERKZEUG_DEBUG_PIN=off

ENTRYPOINT ["python", "jail.py"]
