import secrets
import string

uppercase = True
lowercase = True
numbers = True
punctuations = True

def printSetting():
    print(f"1. Uppercase: {uppercase}")
    print(f"2. Lowercase: {lowercase}")
    print(f"3. Numbers: {numbers}")
    print(f"4. Punctuations: {punctuations}")

def passgen(n):
    charset = ""
    if uppercase:
        charset += string.ascii_uppercase
    if lowercase:
        charset += string.ascii_lowercase
    if numbers:
        charset += string.digits
    if punctuations:
        charset += string.punctuation

    if not charset:
        return "Setting kosong! Tidak ada karakter yang tersedia untuk membuat password."
    
    return ''.join(secrets.choice(charset) for i in range(n))

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



while True:
    try:

        if uppercase == False and lowercase == False and numbers == False and punctuations == False:
            print("Semua setting tidak bisa dimatikan!")
            lowercase = True

        print()
        printSetting()

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

print("\nPassword yang sudah dibuat:")
print(passgen(passwordLength))