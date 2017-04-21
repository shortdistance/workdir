#!/usr/bin/env python
#-*-coding:gbk-*-

import socket
from config import *

def TCPClient():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((Host, Port))

    while 1:
        file = open(LocalFile, 'a')
        data=sock.recv(1024)
        if data:
            print data
            file.write(data)
        file.close()
    sock.close()


if __name__ == '__main__':
    TCPClient()