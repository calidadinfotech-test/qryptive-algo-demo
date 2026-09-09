"""INTENTIONALLY INSECURE testing-only MD5 example. Never use MD5 for security."""

from Crypto.Hash import MD5


message = b"legacy MD5 test"
digest = MD5.new(message).digest()

assert len(digest) == 16
print(f"INSECURE TEST ONLY: MD5 digest {digest.hex()}")
