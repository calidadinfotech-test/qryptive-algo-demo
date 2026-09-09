"""Minimal ChaCha20-Poly1305 authenticated-encryption example."""

import os

from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305


key = ChaCha20Poly1305.generate_key()
nonce = os.urandom(12)
plaintext = b"Qryptive ChaCha20-Poly1305 test"
associated_data = b"authenticated metadata"

ciphertext = ChaCha20Poly1305(key).encrypt(nonce, plaintext, associated_data)
recovered = ChaCha20Poly1305(key).decrypt(nonce, ciphertext, associated_data)

assert recovered == plaintext
print("ChaCha20-Poly1305 round trip passed")
