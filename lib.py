from enum import Enum


class Mode(Enum):
    CRIPTO = 'C'
    DESCRIPTO = 'D'


def complete_blocks(key, file):
    key_length = len(key)
    file_length = len(file)

    if key_length % 2 != 0:
        raise Exception("Invalid Key")

    last_block_size = file_length % key_length

    file = file + ''.join(['0' for i in range(key_length - last_block_size)])

    return [file[i:i + key_length] for i in range(0, len(file), key_length)]


def process(key: str, file: str, mode: Mode):
    key_bits = text_to_bits(key)
    file_bits = text_to_bits(file)

    blocks = complete_blocks(key_bits, file_bits)

    return ''.join(make_xor(x, key_bits) for x in blocks)


def text_to_bits(text: str):
    return bin(int.from_bytes(text.encode(), 'big')).replace('b', '')


def make_xor(right, left):
    left_length = len(left)
    right_length = len(right)

    if left_length != right_length:
        raise Exception('Invalid arguments')

    return ''.join('0' if right[i] == left[i] else '1' for i in range(left_length))
