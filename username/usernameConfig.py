entity = True
adjective = True
numbers = True

def printUserConfig():
    print("\nSettings:")
    print(f"1. Kata Entitas: {entity}")
    print(f"2. Kata Sifat: {adjective}")
    print(f"3. Numbers: {numbers}")

def usernameConfig():

    global entity, adjective, numbers

    while True:
        
        if not (entity or adjective or numbers):
            print("\nSetting kosong! Tidak ada karakter yang tersedia untuk membuat username.")
            entity = True

        printUserConfig()

        try:
            inputSetting = int(input("\nPilih nomor mana yang ingin dinyalakan/dimatikan ([0] untuk selesai): "))
            
            if inputSetting == 1:
                entity = not entity
                continue
            elif inputSetting == 2:
                adjective = not adjective
                continue
            elif inputSetting == 3:
                numbers = not numbers
                continue
            elif inputSetting == 0:
                break

        except ValueError:
            print("Input tidak valid, tolong masukkan angka.")

usernameConfig()