"""
Educational RSA implementation from scratch.

This file intentionally avoids third-party cryptography libraries and generates
temporary keys at runtime. It is for testing and learning only. It does not
include modern padding such as OAEP or PSS, so it is not safe for production.
"""

from __future__ import annotations

import math
import secrets
from dataclasses import dataclass


PUBLIC_EXPONENT = 65537


@dataclass(frozen=True)
class PublicKey:
    n: int
    e: int


@dataclass(frozen=True)
class PrivateKey:
    n: int
    d: int


def _egcd(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        return a, 1, 0

    gcd, x1, y1 = _egcd(b, a % b)
    return gcd, y1, x1 - (a // b) * y1


def _mod_inverse(value: int, modulus: int) -> int:
    gcd, x, _ = _egcd(value, modulus)
    if gcd != 1:
        raise ValueError("inverse does not exist")
    return x % modulus


def _is_probable_prime(candidate: int, rounds: int = 40) -> bool:
    if candidate < 2:
        return False

    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    if candidate in small_primes:
        return True
    if any(candidate % prime == 0 for prime in small_primes):
        return False

    d = candidate - 1
    r = 0
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(rounds):
        witness = secrets.randbelow(candidate - 3) + 2
        x = pow(witness, d, candidate)
        if x in (1, candidate - 1):
            continue

        for _ in range(r - 1):
            x = pow(x, 2, candidate)
            if x == candidate - 1:
                break
        else:
            return False

    return True


def _generate_prime(bits: int) -> int:
    if bits < 16:
        raise ValueError("prime size must be at least 16 bits")

    while True:
        candidate = secrets.randbits(bits)
        candidate |= (1 << (bits - 1)) | 1
        if _is_probable_prime(candidate):
            return candidate


def generate_keypair(bits: int = 1024) -> tuple[PublicKey, PrivateKey]:
    if bits < 512:
        raise ValueError("key size must be at least 512 bits for this demo")

    half_bits = bits // 2

    while True:
        p = _generate_prime(half_bits)
        q = _generate_prime(bits - half_bits)
        if p == q:
            continue

        n = p * q
        phi_n = (p - 1) * (q - 1)
        if math.gcd(PUBLIC_EXPONENT, phi_n) == 1:
            break

    d = _mod_inverse(PUBLIC_EXPONENT, phi_n)
    return PublicKey(n=n, e=PUBLIC_EXPONENT), PrivateKey(n=n, d=d)


def _bytes_to_int(data: bytes) -> int:
    return int.from_bytes(data, "big")


def _int_to_bytes(value: int) -> bytes:
    if value == 0:
        return b"\x00"
    length = (value.bit_length() + 7) // 8
    return value.to_bytes(length, "big")


def encrypt(message: bytes, key: PublicKey) -> int:
    message_int = _bytes_to_int(message)
    if message_int >= key.n:
        raise ValueError("message is too large for the key modulus")
    return pow(message_int, key.e, key.n)


def decrypt(ciphertext: int, key: PrivateKey) -> bytes:
    if not 0 <= ciphertext < key.n:
        raise ValueError("ciphertext is outside the valid range")
    return _int_to_bytes(pow(ciphertext, key.d, key.n))


def sign(message: bytes, key: PrivateKey) -> int:
    message_int = _bytes_to_int(message)
    if message_int >= key.n:
        raise ValueError("message is too large for direct signing")
    return pow(message_int, key.d, key.n)


def verify(message: bytes, signature: int, key: PublicKey) -> bool:
    if not 0 <= signature < key.n:
        return False
    return pow(signature, key.e, key.n) == _bytes_to_int(message)


def main() -> None:
    public_key, private_key = generate_keypair()

    message = b"manual asymmetric demo"
    ciphertext = encrypt(message, public_key)
    recovered = decrypt(ciphertext, private_key)

    signature = sign(message, private_key)
    signature_ok = verify(message, signature, public_key)

    assert recovered == message
    assert signature_ok

    print("Generated temporary keypair.")
    print(f"Modulus bits: {public_key.n.bit_length()}")
    print(f"Ciphertext integer: {ciphertext}")
    print(f"Recovered message: {recovered.decode('utf-8')}")
    print(f"Signature verified: {signature_ok}")
    print("Testing-only implementation; do not use for real security.")


if __name__ == "__main__":
    main()

