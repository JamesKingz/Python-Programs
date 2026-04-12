import os
from cryptography.fernet import Fernet

def load_key():
    """
    Load the encryption key from 'secret.key'.
    If it doesn't exist, generate a new one and save it.
    """
    if not os.path.exists("secret.key"):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
    else:
        with open("secret.key", "rb") as key_file:
            key = key_file.read()
    return key

# Function to decrypt a file
def decrypt_file(filename):
    """
    Decrypts a file that was encrypted with Fernet.
    The decrypted file will overwrite the original filename
    (removing the '.enc' extension).
    """
    key = load_key()
    cipher = Fernet(key)

    # Read the encrypted data
    with open(filename, "rb") as file:
        encrypted_data = file.read()

    # Decrypt the data
    decrypted_data = cipher.decrypt(encrypted_data)

    # Save the decrypted data to a new file
    output_filename = filename.replace(".enc", "")
    with open(output_filename, "wb") as file:
        file.write(decrypted_data)

    print(f"File decrypted successfully: {output_filename}")