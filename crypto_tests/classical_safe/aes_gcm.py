"""Minimal AES-256-GCM authenticated-encryption example."""

import os

from cryptography.hazmat.primitives.ciphers.aead import AESGCM


key = AESGCM.generate_key(bit_length=256)
nonce = os.urandom(12)
plaintext = b"Qryptive AES-GCM test"
associated_data = b"authenticated metadata"

ciphertext = AESGCM(key).encrypt(nonce, plaintext, associated_data)
recovered = AESGCM(key).decrypt(nonce, ciphertext, associated_data)

assert recovered == plaintext
print("AES-256-GCM round trip passed")
