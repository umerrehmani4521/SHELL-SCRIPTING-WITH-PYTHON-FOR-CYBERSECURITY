from cryptography.fernet import Fernet
import sys

# encrypt_file.py
if len(sys.argv) < 2:
    print("Usage: python encrypt_file.py <filename>")
    sys.exit(1)

key = Fernet.generate_key()
cipher = Fernet(key)

with open(sys.argv[1], "rb") as file:
    data = file.read()

encrypted = cipher.encrypt(data)

with open(sys.argv[1] + ".enc", "wb") as file:
    file.write(encrypted)

print(f"File encrypted. Key: {key.decode()}")
