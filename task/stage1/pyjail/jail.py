#!/usr/bin/env python
from __future__ import print_function

import socket
import io, sys
from io import BytesIO as StringIO
import threading


def getSandbox(sock):
    banned = [
        "import","exec","eval","pickle","os","flag","40","subprocess","input","banned","sys"
    ]
    UNSAFE = ['open','file','execfile','compile','reload','__import__','eval','input']
    try:
        for func in UNSAFE:
            del __builtins__.__dict__[func]
    except Exception as a:
        print(str(a))
    while 1:
        old_stdout = sys.stdout
        new_stdout = StringIO()
        sys.stdout = new_stdout
        sock.send(b">>> ")
        data = sock.recv(1024).strip()
        is_banned = False
        for no in banned:
            if no.lower().encode('utf-8') in data.lower():
                sock.send(b"[+] Har jagsaaltand orson :)\n")
                sock.close()
                is_banned = True
                break
        if is_banned:
            sock.close()
            break

        try:
            exec(data)
            result = sys.stdout.getvalue().strip()
            sys.stdout = old_stdout
            sock.send(str(result).encode('utf-8'))
            sock.send(b"\n")
        except Exception as err:
            try:
                sock.send(str(err).encode('utf-8'))
                sock.send(b"\n")
            except Exception as s:
                print(str(s))
            finally:
                sock.close()

if __name__ == "__main__":
    s = socket.socket()
    s.bind(("0.0.0.0", 5000))
    s.listen(256)
    while True:
        print("looop")
        c = s.accept()[0]
        t = threading.Thread(target=getSandbox, args=(c,))
        t.setDaemon = True
        t.start()

