import random

namaHewan = "ref/namaHewan.txt"
kataSifat = "ref/kataSifat.txt"

entity = True
adjective = True
numbers = True

def printUserConfig():
    print("\nSettings:")
    print(f"1. Kata Entitas: {entity}")
    print(f"2. Kata Sifat: {adjective}")
    print(f"3. Nomor: {numbers}")

def usernameConfig():

    global entity, adjective, numbers

    while True:
        
        if not (entity or adjective or numbers):
            print("\nSemua setting tidak bisa dimatikan!")
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

def usernameGenerator():
    
    komponenUsername = []

    if entity:
        with open(namaHewan, encoding="utf-8") as f:
            kata = random.choice(f.read().split()).strip()
            komponenUsername.append(kata)

    if adjective:
        with open(kataSifat, encoding="utf-8") as f:
            sifat = random.choice(f.read().split()).strip()
            komponenUsername.append(sifat)

    if numbers:
        angka = random.randint(10,99)
        komponenUsername.append(str(angka))

    if not komponenUsername:
        return "Error! Setting kosong."

    generatedUsername = ''.join(komponenUsername)

    return print(generatedUsername)

usernameGenerator()
