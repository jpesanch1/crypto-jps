from psec import pinblock


def calculate_iso_0_pinblock(pan, pin):
    return pinblock.encode_pinblock_iso_0(pin, pan).hex()


def calculate_iso_2_pinblock(pin):
    return pinblock.encode_pinblock_iso_2(pin).hex()


def calculate_iso_3_pinblock(pan, pin):
    return pinblock.encode_pinblock_iso_3(pin, pan).hex()


if __name__ == "__main__":
    pan = "4933441234567890"
    pin = "1234"
    print(calculate_iso_0_pinblock(pan, pin))
    print(calculate_iso_2_pinblock(pin))
    print(calculate_iso_3_pinblock(pan, pin))