import psec


def calculate_pin(pan, offset, key, conversion_table):
    return psec.pin.generate_ibm3624_pin(bytes.fromhex(key), conversion_table, offset, pan, 0, 16, 'f')


def calculate_pvv(pan, pin, key):
    return psec.pin.generate_visa_pvv(bytes.fromhex(key), "1", pin, pan)


def calculate_offset(pan, pin, key, conversion_table):
    return psec.pin.generate_ibm3624_offset(bytes.fromhex(key), conversion_table, pin, pan, 0, 16, "f")


if __name__ == "__main__":
    pan = "4940001234567890"
    pin = "1234"
    offset = "2391"
    key = "0123456789abcdeffedcba0987654321"
    conversion_table = "0123456789012345"

    print(calculate_pin(pan, offset, key, conversion_table))
    print(calculate_pvv(pan, pin, key))
    print(calculate_offset(pan, pin, key, conversion_table))
