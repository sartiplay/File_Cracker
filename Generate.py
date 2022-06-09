import sys
import random
import os
from config import *



print("\nMK File Generator Loaded!\n")

try:
    if(sys.argv[1] != ""):
        if(sys.argv[1] == OPKEY):
            print("Generating Opperator File!!\n")
            GenerateOPFile()
            print("Operator File Generated\n")
        else:
            print("This File doesnt take any Arguments\n\n")
            quit()
except:
    pass

FILENAME = input("File Name : ")
FILETYPE = input("File Type : ")

FULLPATH = FILENAME + FILETYPE


try:
    AMMOUNT = int(input("Ammount of Bytes to write ( The bigger the longer it takes ) : "))
except:
    print("Ammount has to be a number")
    pass


print(f"Generating File {FILENAME}{FILETYPE} payload : {AMMOUNT} : bytes")




i = 0

msg = TEMPLATE
if(os.path.exists(OPFILEPATH)):
    print("Operator File Found!")
    msg = ""


while(i < AMMOUNT):
    msg += KEYS[random.randrange(0, len(KEYS))]
    i = i + 1
f = open(FULLPATH, "w")
f.write(msg)
f.close()


print("File Generated!")