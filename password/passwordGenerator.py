import secrets
import string
import pyperclip
import os

# from password.passwordConfig import inputPasswordLength, passwordConfig, uppercase, lowercase, numbers, symbols

uppercase = True
lowercase = True
numbers = True
symbols = True

def printPassConfig():
    print("\nSettings:")
    print(f"1. Uppercase: {uppercase}")
    print(f"2. Lowercase: {lowercase}")
    print(f"3. Numbers: {numbers}")
    print(f"4. Symbols: {symbols}")

def passwordConfig():

    global uppercase, lowercase, numbers, symbols

    while True:

        if not (uppercase or lowercase or numbers or symbols):
            print("\nSemua setting tidak bisa dimatikan!")
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
                symbols = not symbols
                continue
            elif inputSetting == 0:
                break
            else:
                print("\nTolong masukkan angka dari 0-4!")
        except ValueError:
            print("\nInput tidak valid, tolong masukkan angka.")

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

def passwordGenerator():

    passwordLength = inputPasswordLength()
    passwordConfig()

    global uppercase, lowercase, numbers, symbols

    charset = ""
    if uppercase:
        charset += string.ascii_uppercase
    if lowercase:
        charset += string.ascii_lowercase
    if numbers:
        charset += string.digits
    if symbols:
        charset += string.punctuation

    if not charset:
        return "\nSetting kosong! Tidak ada karakter yang tersedia untuk membuat password."
    
    generatedPassword = ''.join(secrets.choice(charset) for i in range(passwordLength))

    pyperclip.copy(generatedPassword)

    os.system('cls')

    return print(f"\nPassword yang sudah dibuat:\n{generatedPassword}")
    # return print(f"\nPassword yang sudah dibuat:\n{''.join(secrets.choice(charset) for i in range(passwordLength))}")