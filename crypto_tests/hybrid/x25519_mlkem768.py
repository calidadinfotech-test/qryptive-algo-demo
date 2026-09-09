"""Conceptual X25519 + ML-KEM-768 hybrid key-establishment example."""

from secrets import compare_digest

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import x25519
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from pqcrypto.kem.ml_kem_768 import decaps, encaps, keygen


def derive_hybrid_key(x25519_secret: bytes, mlkem_secret: bytes) -> bytes:
    """Bind both component secrets into one 256-bit session key."""
    return HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b"qryptive-x25519-ml-kem-768-hybrid-v1",
    ).derive(x25519_secret + mlkem_secret)


alice_x_private = x25519.X25519PrivateKey.generate()
bob_x_private = x25519.X25519PrivateKey.generate()
alice_x_secret = alice_x_private.exchange(bob_x_private.public_key())
bob_x_secret = bob_x_private.exchange(alice_x_private.public_key())

alice_mlkem_public, alice_mlkem_secret = keygen()
mlkem_ciphertext, bob_mlkem_shared = encaps(alice_mlkem_public)
alice_mlkem_shared = decaps(alice_mlkem_secret, mlkem_ciphertext)

alice_final_key = derive_hybrid_key(alice_x_secret, alice_mlkem_shared)
bob_final_key = derive_hybrid_key(bob_x_secret, bob_mlkem_shared)

assert compare_digest(alice_final_key, bob_final_key)
print("X25519 + ML-KEM-768 hybrid key derivation passed")
