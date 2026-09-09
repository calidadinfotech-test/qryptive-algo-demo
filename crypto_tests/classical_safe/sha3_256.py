"""Minimal SHA3-256 hashing example."""

from cryptography.hazmat.primitives import hashes


message = b"Qryptive SHA3-256 test"
hasher = hashes.Hash(hashes.SHA3_256())
hasher.update(message)
digest = hasher.finalize()

assert len(digest) == 32
print(f"SHA3-256 digest: {digest.hex()}")
