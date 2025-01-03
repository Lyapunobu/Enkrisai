import os
import pwinput
from models.dataModel import saveData, loadData
from controllers.usernameGenerator import usernameGenerator
from controllers.passwordGenerator import passwordGenerator

def addItem(username, fernet):
    print("\n=== BUAT ITEM BARU ===")
    
    while True:
        itemName = input("\nMasukkan nama item: ").strip()
        if not itemName:
            print("\nNama item tidak boleh kosong. Silakan coba lagi.")
            continue
        break

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
            passwordInput = pwinput.pwinput("\nMasukkan password: ")
            break
        else:
            print("Tolong masukkan input yang valid. (y/n)")

    data = loadData()

    if itemName in data[username]["items"]:
        os.system('cls')
        print("Item dengan nama tersebut sudah ada. Gunakan nama lain.")
    else:
        encryptedPassword = fernet.encrypt(passwordInput.encode()).decode()
        data[username]["items"][itemName] = {
            "username": usernameInput,
            "password": encryptedPassword
        }
        saveData(data)
        os.system('cls')
        print("Item berhasil ditambahkan!")