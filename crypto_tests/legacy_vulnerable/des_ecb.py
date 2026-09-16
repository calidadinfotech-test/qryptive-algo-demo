"""INTENTIONALLY INSECURE testing-only DES-ECB example. Never use in production."""

from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


key = get_random_bytes(8)
plaintext = b"legacy DES test"
ciphertext = DES.new(key, DES.MODE_ECB).encrypt(pad(plaintext, DES.block_size))
recovered = unpad(DES.new(key, DES.MODE_ECB).decrypt(ciphertext), DES.block_size)

assert recovered == plaintext
print("INSECURE TEST ONLY: DES-ECB round trip passed")
