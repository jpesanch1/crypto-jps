import padding_symmetric
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as pad


def encrypt(plaintext, key, mode, iv, padding="no_padding"):
    padded_text = _get_padded_text(plaintext, padding)
    cipher = Cipher(algorithms.AES(bytes.fromhex(key)), _get_mode(mode, iv))
    encryptor = cipher.encryptor()

    return (encryptor.update(padded_text) + encryptor.finalize()).hex()


def decrypt(ciphertext, key, mode, iv, padding="no_padding"):
    cipher = Cipher(algorithms.AES(bytes.fromhex(key)), _get_mode(mode, iv))
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(bytes.fromhex(ciphertext)) + decryptor.finalize()

    return _get_unpadded_text(decrypted_data.hex(), padding).hex()


def _get_mode(mode, iv):
    switcher = {
        "ecb": modes.ECB(),
        "cbc": modes.CBC(bytes.fromhex(iv)),
        "cfb": modes.CFB(bytes.fromhex(iv)),
        "cfb8": modes.CFB8(bytes.fromhex(iv)),
        "ofb": modes.OFB(bytes.fromhex(iv)),
        "ctr": modes.CTR(bytes.fromhex(iv)),
        "gcm": modes.GCM(bytes.fromhex(iv))
    }
    return switcher.get(mode.lower())


def _get_padded_text(text, padding):
    switcher = {
        "pkcs5": padding_symmetric.pkcs5_padded(text, 16),
        "pkcs7": padding_symmetric.pkcs5_padded(text, 16),
        "ansi_x9_23": padding_symmetric.ansi_x9_23_padded(text, 16),
        "zero_padding": padding_symmetric.zero_padded(text, 16),
        "no_padding": padding_symmetric.no_padding(text)
    }
    return switcher.get(padding.lower())


def _get_unpadded_text(text, padding):
    switcher = {
        "pkcs5": padding_symmetric.pkcs5_unpadded(text),
        "pkcs7": padding_symmetric.pkcs5_unpadded(text),
        "ansi_x9_23": padding_symmetric.ansi_x9_23_unpadded(text),
        "zero_padding": padding_symmetric.zero_unpadded(text),
        "no_padding": padding_symmetric.no_padding(text)
    }
    return switcher.get(padding.lower())


if __name__ == '__main__':
    # key = binascii.hexlify(os.urandom(16))
    # iv = binascii.hexlify(os.urandom(8))
    # message = "0123456789abcdef0123456789abcdef"
    # ciphertext = encrypt(message, key, iv)
    # print(ciphertext)
    # plaintext = decrypt(ciphertext, key, iv)
    # print(plaintext)

    key = "0123456789abcdeffedcba0987654321"
    message = "49400012345678904940001234567890"
    iv = "00000000000000000000000000000000"
    ciphertext = encrypt(message, key, "cbc", iv)
    print(ciphertext)
    plaintext = decrypt(ciphertext, key, "cbc", iv)
    print(plaintext)

    ciphertext = encrypt(message, key, "cbc", iv, "ansi_x9_23")
    print(ciphertext)
    plaintext = decrypt(ciphertext, key, "cbc", iv, "ansi_x9_23")
    print(plaintext)

    pad1 = pad.ANSIX923(128).padder()
    pad1.update(bytes.fromhex(message))
    resultado = pad1.finalize()
    print(resultado.hex())
