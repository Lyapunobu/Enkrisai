import bcrypt

def hash_password(password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed

def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed)

if __name__ == "__main__":
    password = input("Masukkan password: ")
    hashed = hash_password(password)
    print(f"Password hash: {hashed}")

    test_password = input("Masukkan kembali password untuk dicek: ")
    if verify_password(test_password, hashed):
        print("Password cocok!")
    else:
        print("Password tidak cocok.")
