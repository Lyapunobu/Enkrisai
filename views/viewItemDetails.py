import os
import pyperclip
from models.dataModel import saveData, loadData

def viewItemDetails(account_name, account_details, username, fernet): # Menampilkan detail item
    data = loadData()
    show_password = False
    decrypted_password = fernet.decrypt(account_details['password'].encode()).decode()
    
    while True:
        print(f"\n=== ITEM: {account_name} ===")
        stored_username = account_details['username']
        print(f"Username: {stored_username}")
        if show_password:
            print(f"Password: {decrypted_password}")
        else:
            print(f"Password: *****")
        
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
                    saveData(data)
                    os.system('cls')
                    print("Akun berhasil dihapus!")
                    return False
                elif confirm.lower() == 'n':
                    os.system('cls')
                    return False
                else:
                    print("Tolong masukkan input yang valid. (y/n)")
        elif choice == '0':
            os.system('cls')
            return False
        else:
            os.system('cls')
            print("Opsi tidak valid. Silakan pilih lagi.")