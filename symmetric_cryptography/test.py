from symmetric_cryptography import des_cipher

message = "1234567812345678"
key = "123456781234567812345678123456781234567812345678"
iv = "1234567812345678"

if __name__ == "__main__":
    print(des_cipher.encrypt(message, key, iv))