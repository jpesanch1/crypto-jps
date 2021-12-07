from psec import mac
from pyemv import mac as pyemv_mac


def calculate_mac_x9_9(key, data):
    return mac.generate_cbc_mac(bytes.fromhex(key), bytes.fromhex(data), padding=1).hex()


def calculate_mac_x9_19(key, data):
    return pyemv_mac.mac_iso9797_3(bytes.fromhex(key[:16]), bytes.fromhex(key[16:]), bytes.fromhex(data),
                                   padding=1).hex()


def calculate_emv_mac(key, data):
    return pyemv_mac.mac_iso9797_3(bytes.fromhex(key[:16]), bytes.fromhex(key[16:]), bytes.fromhex(data),
                                   padding=2).hex()


if __name__ == "__main__":
    key_des = "0123456789abcdef"
    data = "abcdef123456abcdef123456abcdef123456abcdef123456abcdef123456abcdef123456"

    print(calculate_mac_x9_9(key_des, data))

    key_tdes = "0123456789abcdef1123456789abcdef"

    print(calculate_mac_x9_19(key_tdes, data))
    print(calculate_emv_mac(key_tdes, data))


