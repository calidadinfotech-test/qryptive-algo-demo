"""INTENTIONALLY INSECURE testing-only AES-ECB example. Never use ECB in production."""

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


key = get_random_bytes(32)
plaintext = b"legacy AES-ECB test"
ciphertext = AES.new(key, AES.MODE_ECB).encrypt(pad(plaintext, AES.block_size))
recovered = unpad(AES.new(key, AES.MODE_ECB).decrypt(ciphertext), AES.block_size)

assert recovered == plaintext
print("INSECURE TEST ONLY: AES-ECB round trip passed")
