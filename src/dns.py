import socket

port = 53
ip = '127.0.0.1'

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip, port))

    while True:
        data, addr = sock.recvfrom(512)
        print(f'from: {addr}: {data}')
