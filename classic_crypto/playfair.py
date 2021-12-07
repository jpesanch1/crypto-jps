from secretpy import Playfair, alphabets


def encrypt(text, key, alphabet=alphabets.SPANISH):
    return Playfair().encrypt(text.lower(), key, alphabet)


def decrypt(text, key, alphabet=alphabets.SPANISH):
    return Playfair().decrypt(text.lower(), key, alphabet)


if __name__ == "__main__":
    owner_alphabet = "abcdefghijklmnñopqrstuvwxyz .,"
    text = "esto es una prueba de funcionamiento del cifrado playfair."

    key = "playfair"

    text_encrypted = encrypt(text, key, owner_alphabet)
    text_decrypted = decrypt(text_encrypted, key, owner_alphabet)
    print("encrypted: ", text_encrypted)
    print("decrypted: ", text_decrypted)
