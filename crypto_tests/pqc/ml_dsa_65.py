"""Minimal ML-DSA-65 signature example (FIPS 204)."""

from pqcrypto.sign.ml_dsa_65 import keygen, sign, verify


public_key, secret_key = keygen()
message = b"Qryptive ML-DSA-65 test"
signature = sign(secret_key, message)

verify(public_key, message, signature)
print("ML-DSA-65 signature verification passed")
