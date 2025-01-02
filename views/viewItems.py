import os
from models.dataModel import loadData
from views.viewItemDetails import viewItemDetails

def viewItems(username, fernet):
    while True:
        print("\n=== BRANKAS ENKRISAI ===")
        data = loadData()
        accounts = data[username]["accounts"]
        
        if not accounts:
            print("Belum ada item.")
            return

        print("\nDaftar Item:")
        for i, account_name in enumerate(accounts.keys(), 1):
            print(f"{i}. {account_name}")
        print("\n0. Kembali ke Menu Utama")
        
        choice = input("\nPilih nomor akun (0-" + str(len(accounts)) + "): ")
        
        if choice == '0':
            os.system('cls')
            break
        
        try:
            os.system('cls')
            acc_num = int(choice)
            if 1 <= acc_num <= len(accounts):
                account_name = list(accounts.keys())[acc_num - 1]
                account_deleted = viewItemDetails(account_name, accounts[account_name], username, fernet)
                if account_deleted:
                    continue
            else:
                print("Nomor akun tidak valid.")
        except ValueError:
            print("Masukkan nomor yang valid.")
