def no_padding(data):
    return bytes.fromhex(data)


def zero_padded(data, blocksize_in_bytes):
    data = bytes.fromhex(data)
    while len(data) % blocksize_in_bytes != 0:
        data += bytes.fromhex("00")

    return data


def zero_unpadded(data):
    data = bytearray.fromhex(data)
    while data[-1:] == bytes.fromhex("00"):
        data = data[:-1]

    return data


def pkcs5_padded(data, blocksize_in_bytes):
    data = bytes.fromhex(data)
    data_bytes_length = len(data)
    length_bytes_to_pad = blocksize_in_bytes - data_bytes_length % blocksize_in_bytes
    byte_to_pad = length_bytes_to_pad.to_bytes(1, "big")

    data += byte_to_pad

    while len(data) % blocksize_in_bytes != 0:
        data += byte_to_pad

    return data


def pkcs5_unpadded(data):
    data = bytearray.fromhex(data)
    length_to_delete = int(data[-1:].hex(), 16)
    data = data[:-length_to_delete]

    return data


def ansi_x9_23_padded(data, blocksize_in_bytes):
    data = bytes.fromhex(data)
    data_bytes_length = len(data)
    length_bytes_to_pad = blocksize_in_bytes - data_bytes_length % blocksize_in_bytes
    byte_to_pad = length_bytes_to_pad.to_bytes(1, "big")

    data += bytes.fromhex("00")

    while len(data) % blocksize_in_bytes != 0:
        data += bytes.fromhex("00")

    data_bytearray = bytearray(data)
    data_bytearray[-1:] = byte_to_pad

    return data_bytearray


def ansi_x9_23_unpadded(data):
    data = bytearray.fromhex(data)
    length_to_delete = int(data[-1:].hex(), 16)
    data = data[:-length_to_delete]

    return data


if __name__ == "__main__":
    text_hex = "112233445566778899"
    print(zero_padded(text_hex, 8).hex())
    print(pkcs5_padded(text_hex, 8).hex())
    print(ansi_x9_23_padded(text_hex, 8).hex())

    print(zero_unpadded("11223344556677889900000000000000").hex())
    print(pkcs5_unpadded("11223344556677889907070707070707").hex())
    print(ansi_x9_23_unpadded("11223344556677889900000000000007").hex())


    text_hex = "1122334455667788991122334455667788"
    print(zero_padded(text_hex, 16).hex())
    print(pkcs5_padded(text_hex, 16).hex())
    print(ansi_x9_23_padded(text_hex, 16).hex())

    print(zero_unpadded("1122334455667788991122334455667788000000000000000000000000000000").hex())
    print(pkcs5_unpadded("11223344556677889911223344556677880f0f0f0f0f0f0f0f0f0f0f0f0f0f0f").hex())
    print(ansi_x9_23_unpadded("112233445566778899112233445566778800000000000000000000000000000f").hex())