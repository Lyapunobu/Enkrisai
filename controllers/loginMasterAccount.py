import os
import base64
import bcrypt
from cryptography.fernet import Fernet
from models.dataModel import loadData
from controllers.generateKey import generateKey

def loginMasterAccount():
    print("\n=== LOGIN ENKRISAI ===")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    data = loadData()
    if username not in data:
        os.system('cls')
        print("Username atau password salah. Silakan coba lagi.")
        return None

    # Verify password
    if not bcrypt.checkpw(password.encode(), data[username]["password"].encode()):
        os.system('cls')
        print("Username atau password salah. Silakan coba lagi.")
        return None

    # Mengambil salt dan derive key
    salt = base64.b64decode(data[username]["salt"])
    user_key, _ = generateKey(password, salt)
    
    # Mendekripsi kunci enkripsi personal pengguna
    master_fernet = Fernet(user_key)
    
    try:
        personal_key = master_fernet.decrypt(data[username]["encrypted_key"].encode())
        return username, Fernet(personal_key)
    except Exception:
        print("Error mendekripsi kunci enkripsi. Silakan coba lagi.")
        return None