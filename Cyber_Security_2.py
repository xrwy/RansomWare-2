from cryptography.fernet import Fernet
import os
import key


files = []

for file in os.listdir():
    if file == "Cyber_Security.exe" or file == "Cyber_Security_2.exe":
        continue
    if os.path.isfile(file):
        files.append(file)


for file in files:
    try:
        with open(file, "rb") as the_file:
            contents = the_file.read()
            contents_decrypted = Fernet(key.key).decrypt(contents)

        with open(file, "wb") as the_file:
            the_file.write(contents_decrypted)
            
    except Exception as e:
        continue    
