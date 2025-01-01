import os
import secrets
import string
import json

# Mengimpor fungsi dari file lain
from password.passwordGenerator import passwordGenerator
from password.passwordGeneratorUnused import passwordGenerator as unused_password_generator

# Fungsi untuk menampilkan menu utama
def password_menu():
    while True:
        print("\n=== PASSWORD MENU ===")
        print("1. Generate Password (Using Configured Settings)")
        print("2. Generate Password (Unused Version)")
        print("3. Exit to Main Menu")
        choice = input("Pilih opsi: ")

        if choice == '1':
            generate_password()
        elif choice == '2':
            length = input_password_length()
            password = unused_password_generator(length)
            print(f"Password yang dihasilkan (Unused): {password}")
        elif choice == '3':
            print("Kembali ke menu utama.")
            break
        else:
            print("Opsi tidak valid. Silakan pilih lagi.")

# Fungsi untuk meminta panjang password dari pengguna
def input_password_length():
    while True:
        try:
            password_length = int(input("Panjang password (8-128): "))
            if 8 <= password_length <= 128:
                return password_length
            else:
                print("Tolong masukkan angka dari 8 sampai dengan 128.")
        except ValueError:
            print("Tolong masukkan angka yang valid.")

# Fungsi untuk menghasilkan password menggunakan pengaturan yang dikonfigurasi
def generate_password():
    password_length = input_password_length()
    password = passwordGenerator()
    print(f"Password yang sudah dibuat: {password}")

# Fungsi utama
if __name__ == "__main__":
    password_menu()