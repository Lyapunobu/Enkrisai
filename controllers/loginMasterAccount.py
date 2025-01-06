import os
import base64
import bcrypt
import pwinput
from cryptography.fernet import Fernet
from models.dataModel import loadData
from controllers.generateKey import generateKey

def loginMasterAccount():
    print("\n=== LOGIN ENKRISAI ===")

    username = input("Masukkan username: ").strip()
    password = pwinput.pwinput("Masukkan password: ").strip()

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
    userKey, _ = generateKey(password, salt)
    
    # Mendekripsi kunci enkripsi personal pengguna
    masterFernet = Fernet(userKey)
    
    try:
        personalKey = masterFernet.decrypt(data[username]["encrypted_key"].encode())
        return username, Fernet(personalKey)
    except Exception:
        print("Error mendekripsi kunci enkripsi. Silakan coba lagi.")
        return None