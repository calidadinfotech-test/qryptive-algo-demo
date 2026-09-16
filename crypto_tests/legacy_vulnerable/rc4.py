"""INTENTIONALLY INSECURE testing-only RC4 example. Never use RC4 in production."""

from Crypto.Cipher import ARC4
from Crypto.Random import get_random_bytes


key = get_random_bytes(16)
plaintext = b"legacy RC4 test"
ciphertext = ARC4.new(key).encrypt(plaintext)
recovered = ARC4.new(key).decrypt(ciphertext)

assert recovered == plaintext
print("INSECURE TEST ONLY: RC4 round trip passed")
