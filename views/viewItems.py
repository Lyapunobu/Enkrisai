import os
from models.dataModel import loadData
from views.viewItemDetails import viewItemDetails

def viewItems(username, fernet):
    while True:
        print("\n=== BRANKAS ENKRISAI ===")
        data = loadData()
        items = data[username]["items"]
        
        if not items:
            print("Belum ada item.")
            return

        print("\nDaftar Item:")
        for i, itemName in enumerate(items.keys(), 1):
            print(f"{i}. {itemName}")
        print("\n0. Kembali ke Menu Utama")
        
        choice = input("\nPilih nomor akun (0-" + str(len(items)) + "): ")
        
        if choice == '0':
            os.system('cls')
            break
        
        try:
            os.system('cls')
            accNum = int(choice)
            if 1 <= accNum <= len(items):
                itemName = list(items.keys())[accNum - 1]
                accountDeleted = viewItemDetails(itemName, items[itemName], username, fernet)
                if accountDeleted:
                    continue
            else:
                print("Nomor akun tidak valid.")
        except ValueError:
            print("Masukkan nomor yang valid.")