"""INTENTIONALLY INSECURE testing-only SHA-1 example. Never use SHA-1 for security."""

from Crypto.Hash import SHA1


message = b"legacy SHA-1 test"
digest = SHA1.new(message).digest()

assert len(digest) == 20
print(f"INSECURE TEST ONLY: SHA-1 digest {digest.hex()}")
