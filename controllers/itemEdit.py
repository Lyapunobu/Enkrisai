import os
import pwinput
from models.dataModel import saveData, loadData
from controllers.usernameGenerator import usernameGenerator
from controllers.passwordGenerator import passwordGenerator

def changeItemName(username, oldItemName):
    data = loadData()
    while True:
        newItemName = input("Masukkan nama item baru: ").strip()
        if not newItemName:
            print("Nama item tidak boleh kosong!")
            continue
        if newItemName in data[username]["items"]:
            print("Nama item sudah digunakan. Silakan pilih nama lain.")
            continue
        
        data[username]["items"][newItemName] = data[username]["items"][oldItemName].copy()
        del data[username]["items"][oldItemName]
        saveData(data)
        os.system('cls')
        print("Nama item berhasil diubah!")
        return False

def changeUsername(username, itemName, usernameGenerator):
    data = loadData()
    newUsername = ""
    
    while True:
        confirmNewUserGen = input("Apakah Anda ingin menerapkan username baru secara otomatis? (y/n): ")
        if confirmNewUserGen.lower() == 'y':
            newUsername = usernameGenerator()
            break
        elif confirmNewUserGen.lower() == 'n':
            newUsername = input("\nMasukkan username baru: ")
            break
        else:
            print("Tolong masukkan input yang valid. (y/n)")
    
    data[username]["items"][itemName]["username"] = newUsername
    saveData(data)
    os.system('cls')
    print("Username berhasil diubah menjadi:", newUsername)
    return newUsername

def changePassword(username, itemName, fernet, passwordGenerator):
    data = loadData()
    newPassword = ""

    while True:
        confirmNewPassGen = input("\nApakah kamu ingin menerapkan password baru secara otomatis? (y/n): ")
        if confirmNewPassGen.lower() == 'y':
            newPassword = passwordGenerator()
            break
        elif confirmNewPassGen.lower() == 'n':
            newPassword = pwinput.pwinput("Masukkan password baru: ")
            break
        else:
            print("Tolong masukkan input yang valid. (y/n)")
    
    encryptedPassword = fernet.encrypt(newPassword.encode()).decode()
    data[username]["items"][itemName]["password"] = encryptedPassword
    saveData(data)
    os.system('cls')
    print("Password berhasil diubah!")
    return newPassword

def deleteItem(username, itemName):
    data = loadData()
    while True:
        confirm = input(f"Anda yakin ingin menghapus akun '{itemName}'? (y/n): ")
        if confirm.lower() == 'y':
            del data[username]["items"][itemName]
            saveData(data)
            os.system('cls')
            print("Akun berhasil dihapus!")
            return False
        elif confirm.lower() == 'n':
            os.system('cls')
            return False
        else:
            print("Tolong masukkan input yang valid. (y/n)")