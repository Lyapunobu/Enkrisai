import json
import os
import random

from password.passwordManager import password_menu # Mengimpor fungsi dari passwordManager.py

# File untuk menyimpan data pengguna
USER_DATA_FILE = 'data/user_data.json'
choice = 0

# Fungsi untuk memuat data pengguna dari file JSON
def load_user_data():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

# Fungsi untuk menyimpan data pengguna ke file JSON
def save_user_data(user_data):
    with open(USER_DATA_FILE, 'w') as file:
        json.dump(user_data, file)

# Fungsi untuk melakukan sign in
def sign_in():
    print("\n=== SIGN IN ===")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    user_data = load_user_data()

    if username in user_data:
        print("Username sudah terdaftar. Silakan login.")
    else:
        user_data[username] = password
        save_user_data(user_data)
        print("Akun berhasil dibuat! Silakan login.")

# Fungsi untuk melakukan login
def login():
    print("\n=== LOGIN ===")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    user_data = load_user_data()

    if username in user_data and user_data[username] == password:
        print("Login berhasil!")
        return True  # Mengembalikan True jika login berhasil
    else:
        print("Username atau password salah. Silakan coba lagi.")
        return False  # Mengembalikan False jika login gagal

# Fungsi untuk menampilkan dashboard
def main_dashboard():
    while True:
        print("\n=== DASHBOARD MENU ===")
        print("1. View User Data")
        print("2. Generate Username")
        print("3. Password Manager")  # Opsi untuk mengakses password manager
        print("4. Log Out")
        choice = input("Pilih opsi: ")

        if choice == '1':
            view_user_data()
        elif choice == '2':
            generate_username()
        elif choice == '3':
            password_menu()  # Panggil fungsi password_menu dari passwordManager.py
        elif choice == '4':
            print("Anda telah berhasil log out.")
            break  # Kembali ke menu login
        else:
            print("Opsi tidak valid. Silakan pilih lagi.")

# Fungsi untuk melihat data pengguna
def view_user_data():
    print("\n=== VIEW USER DATA ===")
    try:
        with open(USER_DATA_FILE, 'r') as file:
            user_data = json.load(file)
            for username, password in user_data.items():
                print(f"Username: {username}, Password: {password}")
    except FileNotFoundError:
        print("User  data file not found.")

# Fungsi untuk menghasilkan username (dummy function)
def generate_username():
    print("\n=== GENERATE USERNAME ===")
    # Contoh output username
    username = "user" + str(random.randint(1000, 9999))
    print(f"Username yang dihasilkan: {username}")

# Fungsi untuk menampilkan menu utama
def main_menu():
    while True:
        print("\n=== MENU UTAMA ===")
        print("1. Login")
        print("2. Sign In")
        print("3. Exit")
        choice = input("Pilih opsi: ")

        if choice == '1':
            if login():  # Coba login
                main_dashboard()  # Masuk ke dashboard jika login berhasil
        elif choice == '2':
            sign_in()  # Panggil fungsi sign in
        elif choice == '3':
            print("Keluar dari program. Sampai jumpa!")
            break
        else:
            print("Opsi tidak valid. Silakan pilih lagi.")

# if __name__ == "__main__":
main_menu()