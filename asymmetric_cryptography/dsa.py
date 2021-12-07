from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes


def create_dsa_key(key_size_in_bits):
    private_key = dsa.generate_private_key(
        key_size=key_size_in_bits
    )
    return private_key, private_key.public_key()


def calculate_signature(message, dsa_private_key):
    return dsa_private_key.sign(
        bytes.fromhex(message),
        hashes.SHA256()
    ).hex()


def verify_signature(message, signature, dsa_private_key):
    try:
        dsa_private_key.verify(
            bytes.fromhex(signature),
            bytes.fromhex(message),
            hashes.SHA256()
        )
    except InvalidSignature:
        return False
    return True


if __name__ == "__main__":
    dsa_key = create_dsa_key(2048)
    print(dsa_key[0])
    print(dsa_key[0].private_numbers())
    print(dsa_key[1].public_numbers())

    message = "0123456789abcdef"
    signature = calculate_signature(message, dsa_key[0])
    print("firma: " + signature)
    print(verify_signature(message, signature, dsa_key[1]))
    message = "0123456789abcde1"
    print(verify_signature(message, signature, dsa_key[1]))