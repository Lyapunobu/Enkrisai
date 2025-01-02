import os
from views.viewItems import viewItems
from controllers.addItems import addItem

def dashboard(username, fernet):
    while True:
        print("\n=== MENU ENKRISAI ===")
        print("\n1. Lihat Brankas Enkrisai")
        print("2. Buat Item Baru")
        print("\n0. Log Out")
        choice = input("\nPilih opsi: ")

        if choice == '1':
            os.system('cls')
            viewItems(username, fernet)
        elif choice == '2':
            os.system('cls')
            addItem(username, fernet)
        elif choice == '0':
            os.system('cls')
            print("Log out dari password manager.")
            break
        else:
            os.system('cls')
            print("Opsi tidak valid. Silakan pilih lagi.")