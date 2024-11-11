akun_list = []

def buat_akun(username, password):
    akun = {"username": username, "password": password}
    akun_list.append(akun)
    print(f"Akun dengan username '{username}' berhasil dibuat.")

def login(username, password):
    for akun in akun_list:
        if akun['username'] == username and akun['password'] == password:
            return True
    return False

def main():
    while True:
        print("\nMenu:")
        print("1. Buat akun baru")
        print("2. Login")
        print("3. Keluar")

        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            username = input("Masukkan username baru: ")
            password = input("Masukkan password baru: ")
            buat_akun(username, password)
        elif pilihan == "2":
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")
            if login(username, password):
                print("Login berhasil! Selamat datang di password manager.")
            else:
                print("Username atau password salah!")
        elif pilihan == "3":
            print("Keluar dari program. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

main()
