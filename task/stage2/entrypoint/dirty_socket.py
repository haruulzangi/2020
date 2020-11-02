#!/usr/bin/env python
import socket
import os
import threading
import random
import subprocess

def blacklisted(cmd):
    blacklist = ['cat', 'ls', 'bash', 'sh', 'cp', 'python', 'python3',
                 'echo', 'rm']

    for b in blacklist:
        if str(b) in str(cmd):
            return True

    return False


def getSandbox(conn):
    while 1:
        try:
            data = conn.recv(1024)
            if not data:
                continue

            cmd = data.decode('utf-8').strip('\n')

            if cmd == '':
                print('cmd is empty')
                continue

            if blacklisted(cmd):
                conn.send(b'blacklisted')
                continue

            print(cmd)
            data = subprocess.check_output(cmd.split(" "))
            print(data)
            conn.send(data)
        except Exception as ex:
            print(ex)

if __name__ == "__main__":
    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    try:
        os.remove("/tmp/dirty_socket")
    except OSError:
        pass


    s.bind("/tmp/dirty_socket")
    os.chmod('/tmp/dirty_socket', 4766)
    s.listen(256)
    while True:
        c = s.accept()[0]
        t = threading.Thread(target=getSandbox, args=(c,))
        t.setDaemon = True
        t.start()

