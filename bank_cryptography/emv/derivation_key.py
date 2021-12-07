from pyemv import kd, cvn
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def card_derivation_key(key, pan, psn):
    return kd.derive_icc_mk_a(bytes.fromhex(key), pan, psn).hex()


def session_derivation_key(key, data_to_derive):
    return kd.derive_common_sk(bytes.fromhex(key), r=bytes.fromhex(data_to_derive)).hex()


def session_derivation_key_visa(key, atc):
    return kd.derive_visa_sm_sk(bytes.fromhex(key), bytes.fromhex(atc)).hex()


def session_derivation_key_ac_common():
    cvn18 = cvn.VisaCVN18(
        iss_mk_ac=iss_mk_ac,
        iss_mk_smc=iss_mk_smc,
        iss_mk_smi=iss_mk_smi,
        pan=pan,
        psn=psn
    )
    return cvn18._derive_sk_ac_common(tag_9f36=atc)

def session_derivation_key_sm_common():
    cvn16 = cvn.MasterCardCVN16(
        iss_mk_ac=iss_mk_ac,
        iss_mk_smc=iss_mk_smc,
        iss_mk_smi=iss_mk_smi,
        pan=pan,
        psn=psn
    )
    return cvn16._derive_sk_sm_common(icc_mk_sm=icc_mk_sm, tag_9f26=arqc)


def session_derivation_key_sm_visa():
    cvn18 = cvn.VisaCVN18(
        iss_mk_ac=iss_mk_ac,
        iss_mk_smc=iss_mk_smc,
        iss_mk_smi=iss_mk_smi,
        pan=pan,
        psn=psn
    )
    return cvn18._derive_sk_sm_visa(icc_mk_sm=icc_mk_sm, tag_9f36=atc)


def session_derivation_key_ac_mastercard():
    cvn16 = cvn.MasterCardCVN16(
        iss_mk_ac=bytes.fromhex(iss_mk_ac),
        iss_mk_smc=None,
        iss_mk_smi=None,
        pan=pan,
        psn=psn
    )

    return cvn16._derive_sk_ac_mastercard(tag_9f36=atc, tag_9f37=un)


def session_derivation_key_arpc():
    cvn16 = cvn.MasterCardCVN16(
        iss_mk_ac=iss_mk_ac,
        iss_mk_smc=iss_mk_smc,
        iss_mk_smi=iss_mk_smi,
        pan=pan,
        psn=psn
    )
    return cvn16._derive_sk_arpc_none()


def des_cipher_ecb(plaintext, key):
    cipher = Cipher(algorithms.TripleDES(bytes.fromhex(key)), modes.ECB())
    encryptor = cipher.encryptor()
    return (encryptor.update(bytes.fromhex(plaintext)) + encryptor.finalize()).hex()


if __name__ == "__main__":
    key = "0123456789abcdeffedcba9876543210"

    pan = "4940101234567890"
    psn = "01"

    data = "1122334455667788"
    atc = "1234"

    print(card_derivation_key(key, pan, psn))
    print(session_derivation_key(key, data))
    print(session_derivation_key_visa(key, atc))

    print(des_cipher_ecb("4010123456789001bfefedcba9876ffe", key))
