"""Minimal ECDSA P-256 example; quantum-vulnerable under a cryptographic quantum computer."""

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec


private_key = ec.generate_private_key(ec.SECP256R1())
public_key = private_key.public_key()
message = b"Qryptive ECDSA P-256 test"

signature = private_key.sign(message, ec.ECDSA(hashes.SHA256()))
public_key.verify(signature, message, ec.ECDSA(hashes.SHA256()))
print("ECDSA P-256 signature verification passed (quantum-vulnerable)")
