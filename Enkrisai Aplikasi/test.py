import secrets
import string
import time
import os

def printSetting():
    # Memindahkan kursor ke atas untuk menimpa teks
    print("\033[H\033[J", end="")  # Clear screen with ANSI escape codes
    print("Pengaturan saat ini:")
    print(f"1. Uppercase: {uppercase}")
    print(f"2. Lowercase: {lowercase}")
    print(f"3. Numbers: {numbers}")
    print(f"4. Punctuations: {punctuations}")
    print("Pilih nomor mana yang ingin dinyalakan/dimatikan (atau 0 untuk keluar)")

def passgen(n):
    generatedPassword = ''.join(secrets.choice(string.ascii_uppercase + 
                                 string.ascii_lowercase +
                                 string.digits +
                                 string.punctuation)
                  for i in range(n))
    return generatedPassword

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

uppercase = True
lowercase = True
numbers = True
punctuations = True

while True:
    try:

        printSetting()

        inputSetting = int(input("Pilih nomor mana yang ingin dinyalakan/dimatikan ([0] untuk selesai): "))
        
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

print(passgen(passwordLength))