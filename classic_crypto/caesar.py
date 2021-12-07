from secretpy import Caesar, alphabets


def encrypt(text, key, alphabet=alphabets.SPANISH):
    return Caesar().encrypt(text.lower(), key, alphabet)


def decrypt(text, key, alphabet=alphabets.SPANISH):
    return Caesar().decrypt(text.lower(), key, alphabet)


if __name__ == "__main__":
    owner_alphabet = "abcdefghijklmnñopqrstuvwxyz .,"
    text = "Esto es una prueba de funcionamiento del cifrado Cesar."

    key = 8

    text_encrypted = encrypt(text, key, owner_alphabet)
    text_decrypted = decrypt(text_encrypted, key, owner_alphabet)
    print("encrypted: ", text_encrypted)
    print("decrypted: ", text_decrypted)
