#!/usr/bin/env python
import socket
import threading
import random

def getSandbox(sock):
    while 1:
        notFlag = True
        try:
            sock.sendall(b"Guess the number: ")
            res = sock.recv(1024).strip()
            if res=='1337':
                random_number = random.randint(0,1)
                sock.sendall(str(random_number).encode('utf-8'))
                sock.sendall(str("\n").encode('utf-8'))
                sock.sendall(b"Okey!!! next number: ")
                res = sock.recv(1024).strip()
                print(res)
                print(str(res)=='random_number')
                if res=='random_number' or int(res)==random_number:
                    another_random_number=random.randint(1,2)
                    print(another_random_number)
                    sock.sendall(b"Lucky!!!, next number: \n")
                    res = sock.recv(1024).strip()
                    if res=='another_random_number' or int(res)==another_random_number:
                        last_random_number=random.randint(1337,13371337)*random.randint(6,11)
                        data = "{}\n".format(str(last_random_number)[0:len(str(last_random_number))/3])
                        sock.sendall(data.encode('utf-8'))
                        sock.sendall(b"That's something (!*_*!). Guess the last number: ")
                        res = sock.recv(1024).strip()
                        if str(res)=='last_random_number' or int(res)==last_random_number:
                            sock.sendall(open("flag.txt").read())
                            notFlag = True
                            sock.close()
            if notFlag:
                sock.sendall(b"Wrong number!!!")
                sock.close()
        except Exception as e:
            print(e)
            sock.sendall(b"Not number!!!")
            sock.close()

if __name__ == "__main__":
    s = socket.socket()
    s.bind(("0.0.0.0", 5000))
    s.listen(256)
    while True:
        c = s.accept()[0]
        t = threading.Thread(target=getSandbox, args=(c,))
        t.setDaemon = True
        t.start()
