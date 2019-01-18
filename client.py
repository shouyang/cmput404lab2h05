#!/usr/bin/env python3
import socket

HOST =  "www.google.com"
PORT =  80
PAYLOAD = "GET / HTTP/1.0\r\nHost:{}\r\n\r\n".format(HOST)

BUFFER_SIZE = 1024

def get_request(addr):
    family, socktype, proto, cannonname, sockaddr = addr

    try:
        s = socket.socket(family, socktype, proto)
        s.connect(sockaddr)
        s.sendall(PAYLOAD.encode())
        s.shutdown(socket.SHUT_WR)

        data = b""
        while True:
            _  = s.recv(BUFFER_SIZE)
            data += _
            
            if not _:
                break

        print(data)

    except Exception as e:
        print(e)
    finally:
        s.close()

def main():



    addr_info = socket.getaddrinfo(HOST, PORT)
    for addr in addr_info:
        family, socktype, proto, cannonname, sockaddr = addr

        if family == socket.AF_INET and socktype == socket.SOCK_STREAM:
            print(addr)
            get_request(addr)



if __name__ == "__main__":
    main()