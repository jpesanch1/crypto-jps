from cryptography.hazmat.primitives import hmac, hashes


def calculate(plaintext, key, algorithm):
    h = hmac.HMAC(bytes.fromhex(key), _get_algorithm(algorithm))
    h.update(bytes.fromhex(plaintext))
    return h.finalize().hex()


def _get_algorithm(algorithm):
    switcher = {
        "md5": hashes.MD5(),
        "sha1": hashes.SHA1(),
        "sha256": hashes.SHA256(),
        "sha512": hashes.SHA512()
    }
    return switcher.get(algorithm.lower())


if __name__ == "__main__":
    message = "121314151617181920"
    key = "0123456789abcdeffedcba9876543210"

    print(calculate(message, key, "md5"))
    print(calculate(message, key, "sha1"))
    print(calculate(message, key, "sha256"))
    print(calculate(message, key, "sha512"))
