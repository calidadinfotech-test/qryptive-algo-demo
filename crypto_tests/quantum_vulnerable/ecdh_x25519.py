"""Minimal X25519 ECDH example; quantum-vulnerable under a cryptographic quantum computer."""

from cryptography.hazmat.primitives.asymmetric import x25519


alice_private = x25519.X25519PrivateKey.generate()
bob_private = x25519.X25519PrivateKey.generate()

alice_shared = alice_private.exchange(bob_private.public_key())
bob_shared = bob_private.exchange(alice_private.public_key())

assert alice_shared == bob_shared
print("X25519 shared-secret agreement passed (quantum-vulnerable)")
