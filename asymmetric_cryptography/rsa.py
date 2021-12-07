from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes


def create_rsa_key(key_size_in_bits, public_exponent=65537):
    private_key = rsa.generate_private_key(
        public_exponent=public_exponent,
        key_size=key_size_in_bits
    )
    return private_key, private_key.public_key()


def encrypt(plaintext, rsa_public_key):
    return (rsa_public_key.encrypt(
        bytes.fromhex(plaintext),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    ).hex())


def decrypt(ciphertext, rsa_private_key):
    return (rsa_private_key.decrypt(
        bytes.fromhex(ciphertext),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    ).hex())


def calculate_signature(text, rsa_private_key):
    return rsa_private_key.sign(
        bytes.fromhex(text),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    ).hex()


def verify_signature(text, signature, rsa_public_key):
    try:
        rsa_public_key.verify(
            bytes.fromhex(signature),
            bytes.fromhex(text),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
    except InvalidSignature:
        return False
    return True


if __name__ == "__main__":
    rsa_key = create_rsa_key(2048)
    print(rsa_key[0])
    print(rsa_key[0].private_numbers())
    print(rsa_key[1].public_numbers())

    message = "0123456789abcdef"
    encrypted_message = encrypt(message, rsa_key[1])
    print(encrypted_message)
    decrypted_message = decrypt(encrypted_message, rsa_key[0])
    print(decrypted_message)

    signature = calculate_signature(message, rsa_key[0])
    print("firma: "+signature)
    print(verify_signature(message, signature, rsa_key[1]))
    message = "0123456789abcde1"
    print(verify_signature(message, signature, rsa_key[1]))
