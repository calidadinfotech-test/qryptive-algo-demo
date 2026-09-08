"""Minimal ML-KEM-768 key-encapsulation example (FIPS 203)."""

from secrets import compare_digest

from pqcrypto.kem.ml_kem_768 import decaps, encaps, keygen


public_key, secret_key = keygen()
ciphertext, sender_shared_secret = encaps(public_key)
receiver_shared_secret = decaps(secret_key, ciphertext)

assert compare_digest(sender_shared_secret, receiver_shared_secret)
print("ML-KEM-768 encapsulation/decapsulation passed")
