#!/usr/bin/env python3

import socket

HOST = ""
PORT = 8080

BUFFER_SIZE = 1024

def main():
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind( HOST,PORT )
        s.listen(1)

        while True:

            conn, addr = s.accept()

            print(addr)
            while True:
                data = conn.recv(BUFFER_SIZE)
                conn.sendall(data)
                print(data)
                if not data: break

            conn.sendall(data)
            conn.close()


if __name__ == "__main__":
    main()