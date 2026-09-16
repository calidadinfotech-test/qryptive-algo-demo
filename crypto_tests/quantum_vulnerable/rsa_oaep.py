"""Minimal RSA-OAEP example; quantum-vulnerable under a cryptographic quantum computer."""

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa


private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()
plaintext = b"Qryptive RSA-OAEP test"
oaep = padding.OAEP(
    mgf=padding.MGF1(algorithm=hashes.SHA256()),
    algorithm=hashes.SHA256(),
    label=None,
)

ciphertext = public_key.encrypt(plaintext, oaep)
recovered = private_key.decrypt(ciphertext, oaep)

assert recovered == plaintext
print("RSA-2048 OAEP round trip passed (quantum-vulnerable)")
