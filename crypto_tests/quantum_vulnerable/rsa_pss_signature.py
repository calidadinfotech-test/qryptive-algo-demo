"""Minimal RSA-PSS example; quantum-vulnerable under a cryptographic quantum computer."""

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa


private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()
message = b"Qryptive RSA-PSS test"
pss = padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.DIGEST_LENGTH)

signature = private_key.sign(message, pss, hashes.SHA256())
public_key.verify(signature, message, pss, hashes.SHA256())
print("RSA-2048 PSS signature verification passed (quantum-vulnerable)")
