from pyemv.cvn import MasterCardCVN17


def calculate_arqc(pan, iss_mk_ac, iss_mk_smc, iss_mk_smi,
                   amount, other_amount, country_code, tvr, currency_code, transaction_date,
                   transaction_type, unpredictable_number, aip, atc, cvr, counters):
    cvn17 = MasterCardCVN17(pan=pan,
                      iss_mk_ac=bytes.fromhex(iss_mk_ac),
                      iss_mk_smc=bytes.fromhex(iss_mk_smc),
                      iss_mk_smi=bytes.fromhex(iss_mk_smi)
                      )

    return cvn17.generate_ac(
        tag_9f02=bytes.fromhex(amount),
        tag_9f03=bytes.fromhex(other_amount),
        tag_9f1a=bytes.fromhex(country_code),
        tag_95=bytes.fromhex(tvr),
        tag_5f2a=bytes.fromhex(currency_code),
        tag_9a=bytes.fromhex(transaction_date),
        tag_9c=bytes.fromhex(transaction_type),
        tag_9f37=bytes.fromhex(unpredictable_number),
        tag_82=bytes.fromhex(aip),
        tag_9f36=bytes.fromhex(atc),
        cvr=bytes.fromhex(cvr),
        counters=bytes.fromhex(counters)
    ).hex()


def calculate_arpc(pan, iss_mk_ac, iss_mk_smc, iss_mk_smi,
                   arqc, response_code):
    cvn17 = MasterCardCVN17(pan=pan,
                      iss_mk_ac=bytes.fromhex(iss_mk_ac),
                      iss_mk_smc=bytes.fromhex(iss_mk_smc),
                      iss_mk_smi=bytes.fromhex(iss_mk_smi)
                      )

    return cvn17.generate_arpc(
        tag_9f26=bytes.fromhex(arqc),
        arpc_rc=bytes.fromhex(response_code)
    ).hex()


def encrypt_command_data(pan, iss_mk_ac, iss_mk_smc, iss_mk_smi,
                         arqc, command_data):
    cvn17 = MasterCardCVN17(pan=pan,
                      iss_mk_ac=bytes.fromhex(iss_mk_ac),
                      iss_mk_smc=bytes.fromhex(iss_mk_smc),
                      iss_mk_smi=bytes.fromhex(iss_mk_smi)
                      )

    return cvn17.encrypt_command_data(
        tag_9f26=bytes.fromhex(arqc),
        command_data=bytes.fromhex(command_data)
    ).hex()


def calculate_command_mac(pan, iss_mk_ac, iss_mk_smc, iss_mk_smi,
                          atc, arqc, command_header, command_data):
    cvn17 = MasterCardCVN17(pan=pan,
                      iss_mk_ac=bytes.fromhex(iss_mk_ac),
                      iss_mk_smc=bytes.fromhex(iss_mk_smc),
                      iss_mk_smi=bytes.fromhex(iss_mk_smi)
                      )

    return cvn17.generate_command_mac(
        command_header=bytes.fromhex(command_header),
        tag_9f26=bytes.fromhex(arqc),
        tag_9f36=bytes.fromhex(atc),
        command_data=bytes.fromhex(command_data)
    ).hex()


def calculate_pin_change_command(pan, iss_mk_ac, iss_mk_smc, iss_mk_smi,
                                 pin, atc, arqc):
    cvn17 = MasterCardCVN17(pan=pan,
                      iss_mk_ac=bytes.fromhex(iss_mk_ac),
                      iss_mk_smc=bytes.fromhex(iss_mk_smc),
                      iss_mk_smi=bytes.fromhex(iss_mk_smi)
                      )

    return cvn17.generate_pin_change_command(
        pin=pin,
        tag_9f26=bytes.fromhex(arqc),
        tag_9f36=bytes.fromhex(atc)
    ).hex()


if __name__ == "__main__":
    iss_mk_ac = "0123456789ABCDEFFEDCBA9876543210"
    iss_mk_smi = "FEDCBA98765432100123456789ABCDEF"
    iss_mk_smc = "89ABCDEF0123456776543210FEDCBA98"
    pan = "1234567890123456"
    psn = "00"
    pin = "1234"
    current_pin = "5678"
    amount = "000000004000"
    other_amount = "000000000000"
    country_code = "0124"
    tvr = "8000048000"
    currency_code = "0124"
    transaction_date = "191105"
    transaction_type = "01"
    unpredictable_number = "52BF4585"
    aip = "1800"
    atc = "001C"
    cvr = "03A06010"
    counters = "00000000000322FF"
    arqc = "29CCA15AE665FA2E"
    command_header = "8418000008"
    command_data = "0123456789abcdef"
    response_code = "3030"

    print(calculate_arqc(pan, iss_mk_ac, iss_mk_smc, iss_mk_smi,
                         amount, other_amount, country_code, tvr, currency_code, transaction_date,
                         transaction_type, unpredictable_number, aip, atc, cvr, counters))

    print(calculate_arpc(pan, iss_mk_ac, iss_mk_smc, iss_mk_smi,
                         arqc, response_code))

    print(encrypt_command_data(pan, iss_mk_ac, iss_mk_smc, iss_mk_smi,
                               arqc, command_data))

    print(calculate_command_mac(pan, iss_mk_ac, iss_mk_smc, iss_mk_smi,
                                atc, arqc, command_header, command_data))

    print(calculate_pin_change_command(pan, iss_mk_ac, iss_mk_smc, iss_mk_smi,
                                       pin, atc, arqc))
