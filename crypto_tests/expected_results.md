# Expected Qryptive results

| File | Algorithm | Purpose | Expected classification |
|---|---|---|---|
| `classical_safe/aes_gcm.py` | AES-256-GCM | Authenticated encryption | Safe |
| `classical_safe/chacha20_poly1305.py` | ChaCha20-Poly1305 | Authenticated encryption | Safe |
| `classical_safe/hmac_sha256.py` | HMAC-SHA-256 | Message authentication | Safe |
| `classical_safe/sha3_256.py` | SHA3-256 | Cryptographic hashing | Safe |
| `classical_safe/argon2_password.py` | Argon2id | Password hashing | Safe |
| `quantum_vulnerable/rsa_oaep.py` | RSA-2048 OAEP with SHA-256 | Public-key encryption | Quantum Vulnerable |
| `quantum_vulnerable/rsa_pss_signature.py` | RSA-2048 PSS with SHA-256 | Digital signature | Quantum Vulnerable |
| `quantum_vulnerable/ecdh_x25519.py` | X25519 ECDH | Classical key agreement | Quantum Vulnerable |
| `quantum_vulnerable/ecdsa_p256.py` | ECDSA P-256 with SHA-256 | Digital signature | Quantum Vulnerable |
| `legacy_vulnerable/des_ecb.py` | DES-ECB | Insecure block-cipher detection test | Legacy Vulnerable |
| `legacy_vulnerable/aes_ecb.py` | AES-256-ECB | Insecure block-mode detection test | Legacy Vulnerable |
| `legacy_vulnerable/rc4.py` | RC4 | Insecure stream-cipher detection test | Legacy Vulnerable |
| `legacy_vulnerable/md5_hash.py` | MD5 | Insecure hash detection test | Legacy Vulnerable |
| `legacy_vulnerable/sha1_hash.py` | SHA-1 | Insecure hash detection test | Legacy Vulnerable |
| `pqc/ml_kem_768.py` | ML-KEM-768 | Post-quantum key establishment | PQC Safe |
| `pqc/ml_dsa_65.py` | ML-DSA-65 | Post-quantum digital signature | PQC Safe |
| `pqc/slh_dsa.py` | SLH-DSA-SHA2-128s | Hash-based post-quantum signature | PQC Safe |
| `hybrid/x25519_mlkem768.py` | X25519 + ML-KEM-768 with HKDF-SHA-256 | Hybrid key establishment | Hybrid |

These are the intended scanner findings for the isolated examples. Exact wording or severity can vary by Qryptive scanner version and policy.
