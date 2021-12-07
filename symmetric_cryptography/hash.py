from cryptography.hazmat.primitives import hashes


def calculate(plaintext, algorithm):
    hash = hashes.Hash(_get_algorithm(algorithm))
    hash.update(bytes.fromhex(plaintext))

    return hash.finalize().hex()


def _get_algorithm(algorithm):
    switcher = {
        "md5": hashes.MD5(),
        "sha1": hashes.SHA1(),
        "sha256": hashes.SHA256(),
        "sha512": hashes.SHA512(),
        "sha3_256": hashes.SHA3_256(),
        "sha3_512": hashes.SHA3_512()
    }
    return switcher.get(algorithm.lower())


if __name__ == "__main__":
    message = "121314151617181920"

    print(calculate(message, "md5"))
    print(calculate(message, "sha1"))
    print(calculate(message, "sha256"))
    print(calculate(message, "sha512"))
    print(calculate(message, "sha3_256"))
    print(calculate(message, "sha3_512"))

