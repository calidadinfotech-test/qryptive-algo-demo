# Isolated cryptography examples

This directory is a scanner test corpus of small, independently runnable examples. It is isolated from the repository's application modules. Keys, nonces, salts, and the disposable Argon2id input are generated at runtime; no credentials or persistent private material are included.

The `legacy_vulnerable` examples are intentionally insecure and exist only to test detection. Do not copy them into production code. The `quantum_vulnerable` examples use sound classical constructions but public-key algorithms that are expected to be vulnerable to a sufficiently capable cryptographic quantum computer.

## Setup

Use Python 3.9 or newer in a virtual environment:

```shell
python -m pip install -r crypto_tests/requirements.txt
```

`pqcrypto==1.0.0` is selected because these examples use its current `keygen`/`encaps`/`decaps` and `keygen`/`sign`/`verify` APIs, including standardized SLH-DSA module names.

## Run

Run any example from the repository root, for example:

```shell
python crypto_tests/classical_safe/aes_gcm.py
python crypto_tests/pqc/ml_kem_768.py
python crypto_tests/hybrid/x25519_mlkem768.py
```

To run the complete corpus in PowerShell:

```powershell
Get-ChildItem crypto_tests -Recurse -Filter *.py | ForEach-Object { python $_.FullName }
```

Every script raises an exception or assertion failure on an unsuccessful operation and prints a short success message otherwise. See `expected_results.md` for the intended Qryptive classification of every example.
