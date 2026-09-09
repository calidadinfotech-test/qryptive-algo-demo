# Manual RSA From Scratch

This folder contains a minimal educational implementation of the RSA algorithm
written without third-party cryptography libraries or frameworks.

It is intentionally transparent and labeled. It is not designed to bypass crypto
scanners, and it must not be used for production security.

## What It Demonstrates

- Probable-prime generation with Miller-Rabin
- Key generation from two temporary primes
- Public-key encryption and private-key decryption over integer blocks
- Private-key signing and public-key verification over integer digests

## Run

```powershell
python .\manual_rsa_from_scratch\manual_rsa.py
```

If the Microsoft Store Python stub is active on this machine, use an installed
interpreter or `uv run` instead.

