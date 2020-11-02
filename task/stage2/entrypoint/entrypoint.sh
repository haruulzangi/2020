#! /bin/bash
su -c "python /usr/bin/dirty_socket.py" root &
su -c "/home/chall/.local/bin/gunicorn -b 0.0.0.0:8000 -t 10 -w 4 --log-level debug main:webapp" chall
