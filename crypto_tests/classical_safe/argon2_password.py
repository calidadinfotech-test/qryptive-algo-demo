"""Minimal Argon2id password-hashing and verification example."""

import secrets

from argon2 import PasswordHasher


# This disposable value is generated at runtime and is not a real credential.
temporary_password = secrets.token_urlsafe(24)
hasher = PasswordHasher()
encoded_hash = hasher.hash(temporary_password)

assert hasher.verify(encoded_hash, temporary_password)
print("Argon2id temporary-password verification passed")
