import binascii
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def derivate_key(key, atc):
    atc_padded = atc.zfill(16)
    print(atc_padded)
    atc_padded_ff = xor(atc_padded, "00000000000000ffff").zfill(16)
    print(atc_padded_ff)
    atc_total = atc_padded + atc_padded_ff
    print(atc_total)

    return xor(atc_total, key).zfill(16)


def xor(input_text1, input_text2):
    return hex(int(input_text1, 16) ^ int(input_text2, 16)).upper()[2:]


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
    # Visa Secure Messaging: Session Key derivation finished
    # ****************************************
    # UDK: 94E3194C02105E3B153438D562D5A49D
    # KCV: 086020
    # ATC: 0003
    # —————————————-
    # Session key: 94E3194C02105E38153438D562D55B61
    # KCV: 2268BC
    key = "94E3194C02105E3B153438D562D5A49D"
    atc = "0003"
    print(derivate_key(key, atc))

    # Visa Secure Messaging: MACing operation finished
    # ****************************************
    # Session Key MAC: FB169D8F19C43B62C7258F7C1AE58083
    # KCV: 422C6A
    # MAC Data: 84240002180003EFB5340A1BF07421B3511E3333BF9DC56E1EDF6458BB52B680
    # —————————————-
    # MAC: 8433A315DC674B26
    key = "FB169D8F19C43B62C7258F7C1AE58083"
    text = "84240002180003EFB5340A1BF07421B3511E3333BF9DC56E1EDF6458BB52B680"
    print(mac_calculate(text, key))

    # Session Key Enc: 94E3194C02105E38153438D562D55B61
    # KCV: 2268BC
    # UDK Enc: 64C8621A76A2EA9EF23D5749FE1A64F1
    # KCV: E23347
    # New PIN: 4222
    # —————————————-
    # Encrypted PIN block: B3511E3333BF9DC56E1EDF6458BB52B6
    print(decrypt("B3511E3333BF9DC56E1EDF6458BB52B6", "94E3194C02105E38153438D562D55B61"))


