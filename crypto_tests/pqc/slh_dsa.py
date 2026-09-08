"""Minimal SLH-DSA-SHA2-128s signature example (FIPS 205)."""

from pqcrypto.sign.slh_dsa_sha2_128s import keygen, sign, verify


public_key, secret_key = keygen()
message = b"Qryptive SLH-DSA-SHA2-128s test"
signature = sign(secret_key, message)

verify(public_key, message, signature)
print("SLH-DSA-SHA2-128s signature verification passed")
