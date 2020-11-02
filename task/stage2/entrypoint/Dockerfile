FROM python:3

RUN groupadd -r chall && useradd --no-log-init -r -g chall chall
RUN mkdir /home/chall && chown -R chall:chall /home/chall

COPY ./flag_1.txt /flag.txt
RUN chmod 400 /flag.txt

COPY dirty_socket.py /usr/bin/dirty_socket.py

COPY ./flag.txt /app/flag.txt
RUN chmod 444 /app/flag.txt

CMD python /usr/bin/dirty_socket.py
RUN chmod 4557 /usr/bin/dirty_socket.py

USER chall
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install --user -r requirements.txt

COPY ./chall.py /app/chall.py
COPY ./main.py /app/main.py
COPY ./flag.txt /app/flag.txt

USER root

RUN chown -R chall:chall /app/

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT /entrypoint.sh
