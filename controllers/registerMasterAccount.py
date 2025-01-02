import os
import bcrypt
import base64
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
        password = input("\nMasukkan password: ").strip()
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
    user_key, salt = generateKey(password)
    
    # Membuat kunci enkripsi menggunakan Fernet
    master_fernet = Fernet(user_key)
    
    # Membuat dan mengenkripsi kunci enkripsi personal bagi masing-masing pengguna
    personal_key = Fernet.generate_key()
    encrypted_personal_key = master_fernet.encrypt(personal_key)

    data[username] = {
        "password": bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode(),
        "salt": base64.b64encode(salt).decode(),
        "encrypted_key": encrypted_personal_key.decode(),
        "accounts": {}
    }
    saveData(data)
    os.system('cls')
    print("Akun Enkrisai berhasil dibuat! Silakan login.")