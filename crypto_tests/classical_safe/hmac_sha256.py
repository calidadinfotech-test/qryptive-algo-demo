"""Minimal HMAC-SHA-256 generation and verification example."""

import os

from cryptography.hazmat.primitives import hashes, hmac


key = os.urandom(32)
message = b"Qryptive HMAC-SHA-256 test"

signer = hmac.HMAC(key, hashes.SHA256())
signer.update(message)
tag = signer.finalize()

verifier = hmac.HMAC(key, hashes.SHA256())
verifier.update(message)
verifier.verify(tag)
print("HMAC-SHA-256 verification passed")
