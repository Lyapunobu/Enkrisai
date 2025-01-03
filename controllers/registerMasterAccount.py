import os
import bcrypt
import base64
import pwinput
from cryptography.fernet import Fernet
from models.dataModel import saveData, loadData
from controllers.generateKey import generateKey

def registerMasterAccount():
    os.system('cls')
    print("\n=== REGISTER ENKRISAI ===")

    while True:
        username = input("\nMasukkan username: ").strip()
        if not username:
            print("\nUsername tidak boleh kosong. Silakan coba lagi.")
            continue
        break
    
    while True:
        password = pwinput.pwinput("Masukkan password: ").strip()
        if not password:
            print("\nPassword tidak boleh kosong. Silakan coba lagi.")
            continue
        break

    data = loadData()
    if username in data:
        os.system('cls')
        print("Username sudah terdaftar. Silakan login atau daftar dengan username lain.")
        return

    # Membuat kunci enkripsi dan salt
    userKey, salt = generateKey(password)
    
    # Membuat kunci enkripsi menggunakan Fernet
    masterFernet = Fernet(userKey)
    
    # Membuat dan mengenkripsi kunci enkripsi personal bagi masing-masing pengguna
    personalPey = Fernet.generate_key()
    encryptedPersonalKey = masterFernet.encrypt(personalPey)

    data[username] = {
        "password": bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode(),
        "salt": base64.b64encode(salt).decode(),
        "encrypted_key": encryptedPersonalKey.decode(),
        "items": {}
    }
    saveData(data)
    os.system('cls')
    print("Akun Enkrisai berhasil dibuat! Silakan login.")