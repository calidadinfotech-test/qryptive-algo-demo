import aes_module, rsa_module, fernet_module, quantum_module

def main():
    print("1. AES\n2. RSA\n3. Fernet\n4. Quantum")
    choice = input("Choose algorithm: ")
    
    message = input("Enter message: ")

    if choice == "1":
        key = aes_module.generate_key()
        enc = aes_module.encrypt(message, key)
        print("Encrypted:", enc)
        print("Decrypted:", aes_module.decrypt(enc, key))

    elif choice == "2":
        priv, pub = rsa_module.generate_keys()
        enc = rsa_module.encrypt(message, pub)
        print("Encrypted:", enc)
        print("Decrypted:", rsa_module.decrypt(enc, priv))

    elif choice == "3":
        key = fernet_module.generate_key()
        enc = fernet_module.encrypt(message, key)
        print("Encrypted:", enc)
        print("Decrypted:", fernet_module.decrypt(enc, key))

    elif choice == "4":
        key = quantum_module.generate_key()
        enc = quantum_module.encrypt(message, key)
        print("Encrypted:", enc)
        print("Decrypted:", quantum_module.decrypt(enc, key))

if __name__ == "__main__":
    main()