import json
import socket

from src.utils import decode_header, encode_header, sample_header

port = 53
ip = '127.0.0.1'


def run():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip, port))

    header_dict = sample_header()
    if header_dict['QR'] == 0:  # is query
        print(json.dumps(header_dict, indent=4))
        header_dict['QR'] = 1
        encoded = encode_header(header_dict)
        print(json.dumps(decode_header(encoded), indent=4))
        sock.sendto(encoded, (ip, port))


if __name__ == '__main__':
    run()
