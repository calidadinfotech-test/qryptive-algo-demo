import random

def generate_key(length=16):
    return [random.randint(0, 1) for _ in range(length)]

def encrypt(data, key):
    binary = ''.join(format(ord(c), '08b') for c in data)
    encrypted = ''.join(
        str(int(bit) ^ key[i % len(key)]) for i, bit in enumerate(binary)
    )
    return encrypted

def decrypt(encrypted, key):
    decrypted_binary = ''.join(
        str(int(bit) ^ key[i % len(key)]) for i, bit in enumerate(encrypted)
    )
    
    chars = [
        chr(int(decrypted_binary[i:i+8], 2))
        for i in range(0, len(decrypted_binary), 8)
    ]
    return ''.join(chars)