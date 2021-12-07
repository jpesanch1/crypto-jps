import binascii
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


# def derivate_key(key, atc):
#     atc_padded = atc.zfill(16)
#     print(atc_padded)
#     atc_padded_ff = xor(atc_padded, "00000000000000ffff").zfill(16)
#     print(atc_padded_ff)
#     atc_total = atc_padded + atc_padded_ff
#     print(atc_total)
#
#     return xor(atc_total, key).zfill(16)

#
# def xor(input_text1, input_text2):
#     return hex(int(input_text1, 16) ^ int(input_text2, 16)).upper()[2:]


def encrypt(plaintext, key):
    cipher = Cipher(algorithms.TripleDES(binascii.unhexlify(key)), modes.CBC(binascii.unhexlify("0000000000000000")))
    encryptor = cipher.encryptor()
    return binascii.hexlify(encryptor.update(binascii.unhexlify(plaintext)) + encryptor.finalize())


def decrypt(ciphertext, key):
    cipher = Cipher(algorithms.TripleDES(binascii.unhexlify(key)), modes.CBC(binascii.unhexlify("0000000000000000")))
    decryptor = cipher.decryptor()
    return binascii.hexlify(decryptor.update(binascii.unhexlify(ciphertext)) + decryptor.finalize())


def mac_calculate(text, key):
    key1 = key[0:16]
    key2 = key[16:32]
    mac_part1 = encrypt(text, key1)[-16:]

    mac_part2 = decrypt(mac_part1, key2)
    return encrypt(mac_part2, key1)


if __name__ == '__main__':
    # MasterCard Secure Messaging: MACing operation finished
    # ****************************************
    # Session Key MAC: 1241B9DB1E953A02D5620E8B97418AE8
    # KCV: D338D4
    # MAC Data: 8400000210001051DB71A5DCC47F8A0ED11FDBC43F8F1A80
    # —————————————-
    # MAC: D758292B52F9FF74

    key = "1241B9DB1E953A02D5620E8B97418AE8"
    text = "8400000210001051DB71A5DCC47F8A0ED11FDBC43F8F1A80"
    print(mac_calculate(text, key))

    # MasterCard Secure Messaging: PIN encryption finished
    # ****************************************
    # Session Key Enc: 46AEA9871A61315C4E174FD9EBEB8AAC
    # KCV: A77DB4
    # New PIN: 3356
    # PIN block: Standard EMV
    # —————————————-
    # Plaintext PIN block: 243356FFFFFFFFFF
    # Encrypted PIN block: 0ED11FDBC43F8F1A
    print(decrypt("0ED11FDBC43F8F1A", "46AEA9871A61315C4E174FD9EBEB8AAC"))
