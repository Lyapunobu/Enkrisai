import os
import pyperclip
from controllers.itemEdit import changeItemName, changeUsername, changePassword, deleteItem
from controllers.usernameGenerator import usernameGenerator
from controllers.passwordGenerator import passwordGenerator

def viewItemDetails(itemName, itemDetails, username, fernet):
    showPassword = False
    decryptedPassword = fernet.decrypt(itemDetails['password'].encode()).decode()
    
    while True:
        print(f"\n=== ITEM: {itemName} ===")
        storedUsername = itemDetails['username']
        print(f"Username: {storedUsername}")
        if showPassword:
            print(f"Password: {decryptedPassword}")
        else:
            print(f"Password: *****")
        
        print("\nOpsi:")
        print("\n1. Tampilkan/Sembunyikan Password")
        print("2. Salin Username")
        print("3. Salin Password")
        print("\n4. Edit Nama Item")
        print("5. Edit Username")
        print("6. Edit Password")
        print("7. Hapus Akun")
        print("\n0. Kembali")
        choice = input("\nPilih opsi: ")
        
        if choice == '1':
            os.system('cls')
            showPassword = not showPassword
        
        elif choice == '2':
            pyperclip.copy(storedUsername)
            os.system('cls')
            print("Username berhasil disalin!")
        
        elif choice == '3':
            pyperclip.copy(decryptedPassword)
            os.system('cls')
            print("Password berhasil disalin!")
        
        elif choice == '4':
            return changeItemName(username, itemName)
        
        elif choice == '5':
            itemDetails['username'] = changeUsername(username, itemName, usernameGenerator)
        
        elif choice == '6':
            decryptedPassword = changePassword(username, itemName, fernet, passwordGenerator)
        
        elif choice == '7':
            return deleteItem(username, itemName)
        
        elif choice == '0':
            os.system('cls')
            return False
        
        else:
            os.system('cls')
            print("Opsi tidak valid. Silakan pilih lagi.")