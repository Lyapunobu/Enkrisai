import os
import pwinput
import base64
import bcrypt
from models.dataModel import saveData, loadData
from cryptography.fernet import Fernet
from controllers.generateKey import generateKey

def masterAccountSettings(username, fernet):
   while True:
       print("\n=== MASTER ACCOUNT SETTINGS ===")
       print("\n1. Ganti Master Username")
       print("2. Ganti Master Password")
       print("3. Hapus Master Account")
       print("\n0. Kembali")
       choice = input("\nPilih opsi: ")

       if choice == '1':
           data = loadData()
           while True:
               newUsername = input("\nMasukkan username baru: ").strip()
               if not newUsername:
                   print("Username tidak boleh kosong!")
                   continue
               if newUsername in data:
                   print("Username sudah digunakan. Silakan pilih username lain.")
                   continue
                   
               # Salin data ke username baru
               data[newUsername] = data[username].copy()
               # Hapus data username lama
               del data[username]
               saveData(data)
               os.system('cls')
               print("Username berhasil diubah!")
               return newUsername  # Return username baru ke dashboard
               
       elif choice == '2':
           data = loadData()
           while True:
               currentPassword = pwinput.pwinput("\nMasukkan password saat ini: ")

               if not bcrypt.checkpw(currentPassword.encode(), data[username]["password"].encode()):
                    print("Password salah!")
                    continue

               newPassword = pwinput.pwinput("\nMasukkan password baru: ")
               if not newPassword:
                   print("Password tidak boleh kosong!")
                   continue
                   
               confirmPassword = pwinput.pwinput("Konfirmasi password baru: ")
               if newPassword != confirmPassword:
                   print("Password tidak cocok!")
                   continue
                
               newUserKey, newSalt = generateKey(newPassword)

               newMasterFernet = Fernet(newUserKey)

               newPersonalKey = Fernet.generate_key()
               newEncryptedPersonalKey = newMasterFernet.encrypt(newPersonalKey)

               ######################## UNDONE ###########################
               data[username].update({
                    "password": bcrypt.hashpw(newPassword.encode(), bcrypt.gensalt()).decode(),
                    "salt": base64.b64encode(newSalt).decode(),
                    "encrypted_key": newEncryptedPersonalKey.decode()
                })
               saveData(data)
               os.system('cls')
               print("Password berhasil diubah!")
               break
               
       elif choice == '3':
            data = loadData()
            print("\nPERINGATAN: Menghapus master account akan menghapus semua data yang tersimpan!")
            print("Ketik 'HAPUS' untuk konfirmasi pertama.")
            confirm1 = input("Konfirmasi: ")
            
            if confirm1 == 'HAPUS':
                print("\nKetik username Anda untuk konfirmasi kedua.")
                confirm2 = input("Konfirmasi: ")
                
                if confirm2 == username:
                    print("\nKetik password Anda untuk konfirmasi terakhir.")
                    confirm3 = pwinput.pwinput("Konfirmasi: ")
                    
                    if bcrypt.checkpw(confirm3.encode(), data[username]["password"].encode()):
                        del data[username]
                        saveData(data)
                        os.system('cls')
                        print("Master account berhasil dihapus.")
                        return None
                    else:
                        os.system('cls')
                        print("Password salah. Penghapusan master account dibatalkan.")
                        continue
                    
            os.system('cls')
            print("Penghapusan master account dibatalkan.")
           
       elif choice == '0':
           os.system('cls')
           return username
       else:
           os.system('cls')
           print("Opsi tidak valid. Silakan pilih lagi.")