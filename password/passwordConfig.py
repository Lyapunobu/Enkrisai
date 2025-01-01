uppercase = True
lowercase = True
numbers = True
punctuations = True

def printPassConfig():
    print("\nSettings:")
    print(f"1. Uppercase: {uppercase}")
    print(f"2. Lowercase: {lowercase}")
    print(f"3. Numbers: {numbers}")
    print(f"4. Punctuations: {punctuations}")

def passwordConfig():

    global uppercase, lowercase, numbers, punctuations

    while True:

        if not (uppercase or lowercase or numbers or punctuations):
            print("Semua setting tidak bisa dimatikan!")
            lowercase = True

        printPassConfig()

        try:
            inputSetting = int(input("\nPilih nomor mana yang ingin dinyalakan/dimatikan ([0] untuk selesai): "))
            
            if inputSetting == 1:
                uppercase = not uppercase
                continue
            elif inputSetting == 2:
                lowercase = not lowercase
                continue
            elif inputSetting == 3:
                numbers = not numbers
                continue       
            elif inputSetting == 4:
                punctuations = not punctuations
                continue
            elif inputSetting == 0:
                break
        except ValueError:
            print("Input tidak valid, tolong masukkan angka.")

def inputPasswordLength():
    while True:
        try:

            passwordLength = int(input("Panjang password (8-128): "))

            if passwordLength < 8 or passwordLength > 128:
                print("Tolong masukkan angka dari 8 sampai dengan 128.\n")
                continue
            else:
                break
        
        except ValueError:
            print("Tolong masukkan angka dari 8 sampai dengan 128.\n")
    return passwordLength