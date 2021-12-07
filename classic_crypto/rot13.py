from secretpy import Rot13, alphabets


def encrypt(text, alphabet=alphabets.SPANISH):
    return Rot13().encrypt(text.lower(), 13, alphabet)


def decrypt(text, alphabet=alphabets.SPANISH):
    return Rot13().decrypt(text.lower(), 13, alphabet)


if __name__ == "__main__":
    owner_alphabet = "abcdefghijklmnñopqrstuvwxyz .,"
    text = "esto es una prueba de funcionamiento del cifrado cesar."

    text_encrypted = encrypt(text, owner_alphabet)
    text_decrypted = decrypt(text_encrypted, owner_alphabet)
    print("encrypted: ", text_encrypted)
    print("decrypted: ", text_decrypted)
