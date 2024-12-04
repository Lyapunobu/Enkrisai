import secrets
import string

from password.passwordConfig import inputPasswordLength, passwordConfig, uppercase, lowercase, numbers, punctuations

def passwordGenerator():

    passwordLength = inputPasswordLength()
    passwordConfig()

    global uppercase, lowercase, numbers, punctuations

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
    
    return print(f"\nPassword yang sudah dibuat:\n{''.join(secrets.choice(charset) for i in range(passwordLength))}")