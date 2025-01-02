import json
import os
import bcrypt
import pyperclip
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

DATA_FILE = 'data/users_data.json'

def derive_key(password, salt=None): # Membuat kunci enkripsi dari master password untuk digunakan sebagai kunci enkripsi item
    if salt is None:
        salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key, salt

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    else:
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        with open(DATA_FILE, 'w') as file:
            json.dump({}, file)
        return {}

def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def registerMasterAccount():
    os.system('cls')
    print("\n=== REGISTER ENKRISAI ===")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    data = load_data()
    if username in data:
        os.system('cls')
        print("Username sudah terdaftar. Silakan login atau daftar dengan username lain.")
        return

    # Membuat kunci enkripsi dan salt
    user_key, salt = derive_key(password)
    
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
    save_data(data)
    print("Akun Enkrisai berhasil dibuat! Silakan login.")

def loginMasterAccount():
    print("\n=== LOGIN ENKRISAI ===")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    data = load_data()
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
    user_key, _ = derive_key(password, salt)
    
    # Mendekripsi kunci enkripsi personal pengguna
    master_fernet = Fernet(user_key)
    try:
        personal_key = master_fernet.decrypt(data[username]["encrypted_key"].encode())
        return username, Fernet(personal_key)
    except Exception:
        print("Error mendekripsi kunci enkripsi. Silakan coba lagi.")
        return None

def maskPassword(text): # Masking password dengan bintang
    return '*' * len(text)

def view_item_details(account_name, account_details, username, fernet): # Menampilkan detail item
    data = load_data()
    show_password = False
    decrypted_password = fernet.decrypt(account_details['password'].encode()).decode()
    
    while True:
        print(f"\n=== ITEM: {account_name} ===")
        stored_username = account_details['username']
        print(f"Username: {stored_username}")
        if show_password:
            print(f"Password: {decrypted_password}")
        else:
            print(f"Password: {maskPassword(decrypted_password)}")
        
        print("\nOpsi:")
        print("\n1. Tampilkan/Sembunyikan Password")
        print("2. Salin Username")
        print("3. Salin Password")
        print("4. Hapus Akun")
        print("\n0. Kembali")
        choice = input("\nPilih opsi: ")
        
        if choice == '1':
            os.system('cls')
            show_password = not show_password
        elif choice == '2':
            pyperclip.copy(stored_username)
            os.system('cls')
            print("Username berhasil disalin!")
        elif choice == '3':
            pyperclip.copy(decrypted_password)
            os.system('cls')
            print("Password berhasil disalin!")
        elif choice == '4':
            while True:
                confirm = input(f"Anda yakin ingin menghapus akun '{account_name}'? (y/n): ")
                if confirm.lower() == 'y':
                    del data[username]["accounts"][account_name]
                    save_data(data)
                    os.system('cls')
                    print("Akun berhasil dihapus!")
                    return False
                elif confirm.lower() == 'n':
                    os.system('cls')
                    return False
                else:
                    print("Tolong masukkan input yang valid (y/n).")
        elif choice == '0':
            return False
        else:
            os.system('cls')
            print("Opsi tidak valid. Silakan pilih lagi.")

def view_items(username, fernet):
    while True:
        print("\n=== BRANKAS ENKRISAI ===")
        data = load_data()
        accounts = data[username]["accounts"]
        
        if not accounts:
            print("Belum ada item.")
            return

        print("\nDaftar Item:")
        for i, account_name in enumerate(accounts.keys(), 1):
            print(f"{i}. {account_name}")
        print("\n0. Kembali ke Menu Utama")
        
        choice = input("\nPilih nomor akun (0-" + str(len(accounts)) + "): ")
        
        if choice == '0':
            os.system('cls')
            break
        
        try:
            os.system('cls')
            acc_num = int(choice)
            if 1 <= acc_num <= len(accounts):
                account_name = list(accounts.keys())[acc_num - 1]
                account_deleted = view_item_details(account_name, accounts[account_name], username, fernet)
                if account_deleted:
                    continue  # Me-refresh list item
            else:
                print("Nomor akun tidak valid.")
        except ValueError:
            print("Masukkan nomor yang valid.")

def add_item(username, fernet):
    print("\n=== BUAT ITEM BARU ===")
    account_name = input("Masukkan nama akun: ")
    username_input = input("Masukkan username: ")
    password = input("Masukkan password: ")

    data = load_data()

    if account_name in data[username]["accounts"]:
        os.system('cls')
        print("Akun dengan nama tersebut sudah ada. Gunakan nama lain.")
    else:
        encrypted_password = fernet.encrypt(password.encode()).decode()
        data[username]["accounts"][account_name] = {
            "username": username_input,
            "password": encrypted_password
        }
        save_data(data)
        os.system('cls')
        print("Item berhasil ditambahkan!")

def dashboard(username, fernet):
    while True:
        print("\n=== MENU ENKRISAI ===")
        print("\n1. Lihat Brankas Enkrisai")
        print("2. Buat Item Baru")
        print("\n0. Log Out")
        choice = input("\nPilih opsi: ")

        if choice == '1':
            os.system('cls')
            view_items(username, fernet)
        elif choice == '2':
            os.system('cls')
            add_item(username, fernet)
        elif choice == '0':
            os.system('cls')
            print("Log out dari password manager.")
            break
        else:
            os.system('cls')
            print("Opsi tidak valid. Silakan pilih lagi.")

def main_menu():
    while True:
        print("\n=== SELAMAT DATANG DI ENKRISAI ===")
        print("\n1. Login")
        print("2. Register")
        print("\n0. Exit")
        choice = input("\nPilih opsi: ")

        if choice == '1':
            os.system('cls')
            login_result = loginMasterAccount()
            if login_result:
                username, fernet = login_result
                os.system('cls')
                print("Login berhasil! Selamat datang di Enkrisai.")
                dashboard(username, fernet)
        elif choice == '2':
            registerMasterAccount()
        elif choice == '0':
            os.system('cls')
            print("Keluar dari program. Sampai jumpa!")
            break
        else:
            os.system('cls')
            print("Opsi tidak valid. Silakan pilih lagi.")

if __name__ == "__main__":
    main_menu()