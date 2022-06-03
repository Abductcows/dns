import socket
import time

port = 53
ip = '127.0.0.1'

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        time.sleep(1)
        sock.sendto('test hello'.encode('utf-8'), (ip, port))
