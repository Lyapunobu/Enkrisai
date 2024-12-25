import secrets
import string
import random

list_kosakata_sementara = ["kucing", "ayam", "pelangi", "merah", "mawar",  
                           "biru", "kelinci", "keren", "delima", "tertawa"]

def usergen(n, jumlah_kata):
    kata = random.sample(list_kosakata_sementara, jumlah_kata)
    username = ''.join(kata)
    n -= len(username)
    if n > 0:
        charset = string.digits
        username += ''.join(secrets.choice(charset) for i in range(n))
    return username

def inputUsernameLength():
    while True:
        try:
            usernameLength = int(input("Panjang username (5-20): "))
            if usernameLength < 5 or usernameLength > 20:
                print("Tolong masukkan angka dari 5 sampai dengan 20.\n")
                continue
            else:
                break
        except ValueError:
            print("Tolong masukkan angka dari 5 sampai dengan 20.\n")
    return usernameLength

def inputWordCount():
    while True:
        try:
            word_count = int(input("Jumlah kata dalam username (1-3): "))
            if word_count < 1 or word_count > 3:
                print("Tolong masukkan angka antara 1 dan 3.\n")
                continue
            else:
                break
        except ValueError:
            print("Tolong masukkan angka antara 1 dan 3.\n")
    return word_count

usernameLength = inputUsernameLength()
word_count = inputWordCount()

print("\nUsername yang sudah dibuat:")
print(usergen(usernameLength, word_count))