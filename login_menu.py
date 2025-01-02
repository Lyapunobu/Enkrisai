import json
import os
import bcrypt
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

# File paths
DATA_FILE = 'data/users_data.json'
MASTER_KEY_FILE = 'data/master.key'

def generate_master_key():
    """Generate master encryption key if it doesn't exist"""
    if os.path.exists(MASTER_KEY_FILE):
        with open(MASTER_KEY_FILE, 'rb') as file:
            return file.read()
    else:
        key = Fernet.generate_key()
        os.makedirs(os.path.dirname(MASTER_KEY_FILE), exist_ok=True)
        with open(MASTER_KEY_FILE, 'wb') as file:
            file.write(key)
        return key

def derive_key_from_password(password, salt=None):
    """Derive an encryption key from the master password"""
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
    """Load data from JSON file"""
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
    """Save data to JSON file"""
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def register_master_account():
    print("\n=== REGISTER MASTER ACCOUNT ===")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    data = load_data()
    if username in data:
        print("Username sudah terdaftar. Silakan login.")
        return

    # Generate user's encryption key and salt
    user_key, salt = derive_key_from_password(password)
    
    # Create Fernet instance for master key encryption
    master_fernet = Fernet(user_key)
    
    # Generate and encrypt user's personal encryption key
    personal_key = Fernet.generate_key()
    encrypted_personal_key = master_fernet.encrypt(personal_key)

    # Store user data
    data[username] = {
        "password": bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode(),
        "salt": base64.b64encode(salt).decode(),
        "encrypted_key": encrypted_personal_key.decode(),
        "accounts": {}
    }
    save_data(data)
    print("Master account berhasil dibuat! Silakan login.")

def login_master_account():
    print("\n=== LOGIN MASTER ACCOUNT ===")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    data = load_data()
    if username not in data:
        print("Username atau password salah. Silakan coba lagi.")
        return None

    # Verify password
    if not bcrypt.checkpw(password.encode(), data[username]["password"].encode()):
        print("Username atau password salah. Silakan coba lagi.")
        return None

    # Retrieve user's salt and derive key
    salt = base64.b64decode(data[username]["salt"])
    user_key, _ = derive_key_from_password(password, salt)
    
    # Decrypt user's personal encryption key
    master_fernet = Fernet(user_key)
    try:
        personal_key = master_fernet.decrypt(data[username]["encrypted_key"].encode())
        return username, Fernet(personal_key)
    except Exception:
        print("Error decrypting user key. Please try again.")
        return None

def mask_string(text):
    """Masking string dengan bintang"""
    return '*' * len(text)

def view_account_details(account_name, account_details, username, fernet):
    """Menampilkan detail akun dengan opsi untuk menampilkan/menyembunyikan password"""
    data = load_data()
    show_password = False
    decrypted_password = fernet.decrypt(account_details['password'].encode()).decode()
    
    while True:
        print(f"\n=== DETAIL AKUN: {account_name} ===")
        stored_username = account_details['username']
        print(f"Username: {stored_username}")
        if show_password:
            print(f"Password: {decrypted_password}")
        else:
            print(f"Password: {mask_string(decrypted_password)}")
        
        print("\nOpsi:")
        print("1. Tampilkan/Sembunyikan Password")
        print("2. Hapus Akun")
        print("0. Kembali")
        choice = input("Pilih opsi: ")
        
        if choice == '1':
            show_password = not show_password
        elif choice == '2':
            confirm = input(f"Anda yakin ingin menghapus akun '{account_name}'? (y/n): ")
            if confirm.lower() == 'y':
                del data[username]["accounts"][account_name]
                save_data(data)
                print("Akun berhasil dihapus!")
                return True  # Indicate account was deleted
        elif choice == '0':
            return False
        else:
            print("Opsi tidak valid. Silakan pilih lagi.")

def view_passwords(username, fernet):
    while True:
        print("\n=== STORED PASSWORDS ===")
        data = load_data()
        accounts = data[username]["accounts"]
        
        if not accounts:
            print("Belum ada data tersimpan.")
            return

        # Tampilkan daftar akun
        print("\nDaftar Akun:")
        for i, account_name in enumerate(accounts.keys(), 1):
            print(f"{i}. {account_name}")
        print("\n0. Kembali ke Menu Utama")
        
        choice = input("\nPilih nomor akun (0-" + str(len(accounts)) + "): ")
        
        if choice == '0':
            break
        
        try:
            acc_num = int(choice)
            if 1 <= acc_num <= len(accounts):
                account_name = list(accounts.keys())[acc_num - 1]
                account_deleted = view_account_details(account_name, accounts[account_name], username, fernet)
                if account_deleted:
                    continue  # Refresh the account list
            else:
                print("Nomor akun tidak valid.")
        except ValueError:
            print("Masukkan nomor yang valid.")

def add_password(username, fernet):
    print("\n=== ADD NEW PASSWORD ===")
    account_name = input("Masukkan nama akun: ")
    username_input = input("Masukkan username: ")
    password = input("Masukkan password: ")

    data = load_data()

    if account_name in data[username]["accounts"]:
        print("Akun dengan nama tersebut sudah ada. Gunakan nama lain.")
    else:
        encrypted_password = fernet.encrypt(password.encode()).decode()
        data[username]["accounts"][account_name] = {
            "username": username_input,
            "password": encrypted_password
        }
        save_data(data)
        print("Data akun berhasil ditambahkan!")

def password_menu(username, fernet):
    while True:
        print("\n=== PASSWORD MANAGER MENU ===")
        print("1. View Stored Passwords")
        print("2. Add New Password")
        print("0. Log Out")
        choice = input("Pilih opsi: ")

        if choice == '1':
            view_passwords(username, fernet)
        elif choice == '2':
            add_password(username, fernet)
        elif choice == '0':
            print("Log out dari password manager.")
            break
        else:
            print("Opsi tidak valid. Silakan pilih lagi.")

def main_menu():
    while True:
        print("\n=== MAIN MENU ===")
        print("1. Login Master Account")
        print("2. Register Master Account")
        print("0. Exit")
        choice = input("Pilih opsi: ")

        if choice == '1':
            login_result = login_master_account()
            if login_result:
                username, fernet = login_result
                password_menu(username, fernet)
        elif choice == '2':
            register_master_account()
        elif choice == '0':
            print("Keluar dari program. Sampai jumpa!")
            break
        else:
            print("Opsi tidak valid. Silakan pilih lagi.")

if __name__ == "__main__":
    main_menu()