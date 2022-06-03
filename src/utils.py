import json
from collections import OrderedDict

from bitarray import bitarray


def get_base_mask():
    return int(64 * '1', 2)


# name - size in bits
fields = OrderedDict([
    ('ID', 16),
    ('QR', 1),
    ('OPCODE', 4),
    ('AA', 1),
    ('TC', 1),
    ('RD', 1),
    ('RA', 1),
    ('Z', 3),
    ('RCODE', 4),
    ('QDCOUNT', 16),
    ('ANCOUNT', 16),
    ('NSCOUNT', 16),
    ('ARCOUNT', 16),
])


def decode_header(header: bytes) -> OrderedDict:
    cursor = 0
    pairs = []

    for field, size in fields.items():
        pairs.append(
            (field, get_header_value(header[cursor // 8:], cursor % 8, size))
        )
    return OrderedDict(pairs)


def encode_header(header: dict) -> bytes:
    result = bitarray()
    for field_name, value in header.items():
        value_str = '{0:b}'.format(value).zfill(fields[field_name])
        result.extend(value_str)
    return result.tobytes()


def sample_header():
    return json.loads(
        """
            {
                "ID": 20669,
                "QR": 0,
                "OPCODE": 0,
                "AA": 0,
                "TC": 0,
                "RD": 1,
                "RA": 0,
                "Z": 0,
                "RCODE": 0,
                "QDCOUNT": 256,
                "ANCOUNT": 0,
                "NSCOUNT": 0,
                "ARCOUNT": 0
            }
        """
    )


base_mask = get_base_mask()


def select_bits(number, number_length, start, length):
    result = number >> (number_length - start - length)
    result = result & (base_mask >> (64 - length))
    return result


BITS_PER_BYTE = 8


def get_header_value(header_row, start=0, length=16):
    val = int.from_bytes(header_row, 'little')
    return select_bits(
        val,
        BITS_PER_BYTE * len(header_row),
        start,
        length
    )


if __name__ == '__main__':
    print(sum(fields.values()) / 8)
