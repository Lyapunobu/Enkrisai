import os
from models.dataModel import saveData, loadData
from controllers.usernameGenerator import usernameGenerator
from controllers.passwordGenerator import passwordGenerator

def addItem(username, fernet):
    print("\n=== BUAT ITEM BARU ===")
    account_name = input("\nMasukkan nama item: ")
    usernameInput = ""
    passwordInput = ""

    while True:
        confirmUserGen = input("\nApakah Anda ingin menerapkan username secara otomatis? (y/n): ")
        if confirmUserGen.lower() == 'y':
            usernameInput = usernameGenerator()
            print("\nGenerated username:", usernameInput)
            break
        elif confirmUserGen.lower() == 'n':
            usernameInput = input("\nMasukkan username: ")
            break
        else:
            print("Tolong masukkan input yang valid. (y/n)")

    while True:
        confirmPassGen = input("\nApakah kamu ingin menerapkan password secara otomatis? (y/n): ")
        if confirmPassGen.lower() == 'y':
            passwordInput = passwordGenerator()
            break
        elif confirmPassGen.lower() == 'n':
            passwordInput = input("\nMasukkan password: ")
            break

    data = loadData()

    if account_name in data[username]["accounts"]:
        os.system('cls')
        print("Akun dengan nama tersebut sudah ada. Gunakan nama lain.")
    else:
        encrypted_password = fernet.encrypt(passwordInput.encode()).decode()
        data[username]["accounts"][account_name] = {
            "username": usernameInput,
            "password": encrypted_password
        }
        saveData(data)
        os.system('cls')
        print("Item berhasil ditambahkan!")