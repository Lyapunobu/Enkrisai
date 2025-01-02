def main_menu():
    while True:
        print("\n=== SELAMAT DATANG DI ENKRISAI ===")
        print("\n1. Login")
        print("2. Register")
        print("\n0. Exit")
        choice = input("\nPilih opsi: ")

        if choice == '1':
            os.system('cls')
            login_result = loginMasterAccount()
            if login_result:
                username, fernet = login_result
                os.system('cls')
                print("Login berhasil! Selamat datang di Enkrisai.")
                dashboard(username, fernet)
        elif choice == '2':
            registerMasterAccount()
        elif choice == '0':
            os.system('cls')
            print("Keluar dari Enkrisai... Sampai jumpa!")
            break
        else:
            os.system('cls')
            print("Opsi tidak valid. Silakan pilih lagi.")

"""     if __name__ == "__main__":
        main_menu() """