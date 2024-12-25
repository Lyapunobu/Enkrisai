import random

namaHewan = "ref/namaHewan.txt"
kataSifat = "ref/kataSifat.txt"

def usernameGenerator():

    with open(namaHewan, encoding="utf-8") as f:
        kata = random.choice(f.read().split()).strip()

    with open(kataSifat, encoding="utf-8") as f:
        sifat = random.choice(f.read().split()).strip()

    angka = random.randint(10,99)

    return f"{kata}{sifat}{angka}"


print(usernameGenerator())