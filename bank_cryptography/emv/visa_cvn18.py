from pyemv.cvn import VisaCVN18


def calculate_arqc(pan, iss_mk_ac, iss_mk_smc, iss_mk_smi,
                   amount, other_amount, country_code, tvr, currency_code, transaction_date,
                   transaction_type, unpredictable_number, aip, atc, iad):
    cvn18 = VisaCVN18(pan=pan,
                      iss_mk_ac=bytes.fromhex(iss_mk_ac),
                      iss_mk_smc=bytes.fromhex(iss_mk_smc),
                      iss_mk_smi=bytes.fromhex(iss_mk_smi)
                      )

    return cvn18.generate_ac(
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
        tag_9f10=bytes.fromhex(iad)
    ).hex()


def calculate_arpc(pan, iss_mk_ac, iss_mk_smc, iss_mk_smi,
                   atc, arqc, csu):
    cvn18 = VisaCVN18(pan=pan,
                      iss_mk_ac=bytes.fromhex(iss_mk_ac),
                      iss_mk_smc=bytes.fromhex(iss_mk_smc),
                      iss_mk_smi=bytes.fromhex(iss_mk_smi)
                      )

    return cvn18.generate_arpc(
        tag_9f26=bytes.fromhex(arqc),
        tag_9f36=bytes.fromhex(atc),
        csu=bytes.fromhex(csu)
    ).hex()


def encrypt_command_data(pan, iss_mk_ac, iss_mk_smc, iss_mk_smi,
                         atc, command_data):
    cvn18 = VisaCVN18(pan=pan,
                      iss_mk_ac=bytes.fromhex(iss_mk_ac),
                      iss_mk_smc=bytes.fromhex(iss_mk_smc),
                      iss_mk_smi=bytes.fromhex(iss_mk_smi)
                      )

    return cvn18.encrypt_command_data(
        tag_9f36=bytes.fromhex(atc),
        command_data=bytes.fromhex(command_data)
    ).hex()


def calculate_command_mac(pan, iss_mk_ac, iss_mk_smc, iss_mk_smi,
                          atc, arqc, command_header, command_data):
    cvn18 = VisaCVN18(pan=pan,
                      iss_mk_ac=bytes.fromhex(iss_mk_ac),
                      iss_mk_smc=bytes.fromhex(iss_mk_smc),
                      iss_mk_smi=bytes.fromhex(iss_mk_smi)
                      )

    return cvn18.generate_command_mac(
        command_header=bytes.fromhex(command_header),
        tag_9f26=bytes.fromhex(arqc),
        tag_9f36=bytes.fromhex(atc),
        command_data=bytes.fromhex(command_data)
    ).hex()


def calculate_pin_change_command(pan, iss_mk_ac, iss_mk_smc, iss_mk_smi,
                                 pin, current_pin, atc, arqc):
    cvn18 = VisaCVN18(pan=pan,
                      iss_mk_ac=bytes.fromhex(iss_mk_ac),
                      iss_mk_smc=bytes.fromhex(iss_mk_smc),
                      iss_mk_smi=bytes.fromhex(iss_mk_smi)
                      )

    return cvn18.generate_pin_change_command(
        pin=pin,
        tag_9f26=bytes.fromhex(arqc),
        tag_9f36=bytes.fromhex(atc),
        current_pin=current_pin
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
    iad = "06011203A0B800"
    arqc = "29CCA15AE665FA2E"
    command_header = "8418000008"
    command_data = "0123456789abcdef"
    csu = "00000000"

    print(calculate_arqc(pan, iss_mk_ac, iss_mk_smc, iss_mk_smi,
                         amount, other_amount, country_code, tvr, currency_code, transaction_date,
                         transaction_type, unpredictable_number, aip, atc, iad))

    print(calculate_arpc(pan, iss_mk_ac, iss_mk_smc, iss_mk_smi,
                         atc, arqc, csu))

    print(encrypt_command_data(pan, iss_mk_ac, iss_mk_smc, iss_mk_smi,
                               atc, command_data))

    print(calculate_command_mac(pan, iss_mk_ac, iss_mk_smc, iss_mk_smi,
                                atc, arqc, command_header, command_data))

    print(calculate_pin_change_command(pan, iss_mk_ac, iss_mk_smc, iss_mk_smi,
                                       pin, current_pin, atc, arqc))
