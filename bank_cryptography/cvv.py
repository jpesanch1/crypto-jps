import psec


def calculate_cvv(pan, expiration_date, service_code, key):
    return psec.cvv.generate_cvv(bytes.fromhex(key), pan, expiration_date, service_code)


def calculate_cvv2(pan, expiration_date, key):
    return psec.cvv.generate_cvv(bytes.fromhex(key), pan, expiration_date, service_code="000")


if __name__ == "__main__":
    pan = "4940001234567890"
    expiration_date = "1228"
    service_code = "101"
    key = "0123456789abcdeffedcba0987654321"

    print(calculate_cvv(pan, expiration_date, service_code, key))
    print(calculate_cvv2(pan, expiration_date, key))
