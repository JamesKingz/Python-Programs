import os
from cryptography.fernet import Fernet

# Generate or load a key
def load_key():
    if not os.path.exists("secret.key"):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
    else:
        with open("secret.key", "rb") as key_file:
            key = key_file.read()
    return key

def encrypt_file(filename):
    key = load_key()
    cipher = Fernet(key)
    with open(filename, "rb") as file:
        data = file.read()
    encrypted = cipher.encrypt(data)
    with open(filename + ".enc", "wb") as file:
        file.write(encrypted)