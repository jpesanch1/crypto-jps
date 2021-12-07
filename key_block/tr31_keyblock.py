import os

# C805321ACF492D2256C3220BE81D542AC8B1DAC9AA30BD7B94E4185F8473A005
# CB8BD9C7812EAD16

from psec import tr31
from symmetric_cryptography import des_cipher



key = os.urandom(32)
print(key.hex())

h = tr31.Header()
h.version_id = "B"
h.key_usage = "P0"
h.algorithm = "T"
h.mode_of_use = "E"
h.version_num = "00"
h.exportability = "N"
# h.blocks["KS"] = "00604B120F9292"
h.load(str(h))
print(h)

# k = tr31.KeyBlock()


print(tr31.Header())
print(tr31.Blocks())
print(tr31.KeyBlock(kbpk=key))

header = tr31.Header(
    version_id="B",  # Version B as recommended for TDES
    key_usage="P0",  # PIN Encryption
    algorithm="T",  # TDES
    mode_of_use="E",  # Encryption only
    version_num="00",  # No version
    exportability="N"  # Not exportable
)
kb = tr31.KeyBlock(kbpk=b"FFFFFFFFEEEEEEEE", header=header)
keyblock = kb.wrap(key=b"CCCCCCCCDDDDDDDD")  # doctest: +SKIP
print(keyblock)
#    'B0096P0TE00N0000C805321ACF492D2256C3220BE81D542AC8B1DAC9AA30BD7B94E4185F8473A005CB8BD9C7812EAD16'
str(kb.header)
#    'B0016P0TE00N0000'

keys = kb._b_derive()
print(keys[0].hex())
print(keys[1].hex())

print(des_cipher.decrypt("a6b5eac80f3252be0af230eeddc6ee7d", "FFFFFFFFEEEEEEEE", "cbc",
                         "0000000000000000"))

