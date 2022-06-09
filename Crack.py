import os
import os.path
import sys
import random
from config import *


isOp = False


CustomOverride = False
OverrideFile = True


OverrideBytes = False   #If True the Bytes to Write can be Overriten
hasADKey = False        #ADKey = Admin Key = Opperator Permissions
TypesToCrypt = ["destroy", "cracked", "small"]  #All The Types of Breaking
TypeSelected = ""
WordFilePath = ""
BytesToWrite = 100000   #Can be Overriten if OverrideBytes = True

#   Check if Operator File has been found!
if(os.path.exists(CURR_FILE_PATH + OP_FILENAME)):
    print("Opperator File Found!\nContinue with OP Permissions")
    isOp = True


def UserHelpDisplay(): #Display User Help with all Commands
    print("Word-Cracker Arguments :\n-d = Destroy\n-c = Cracked\n-s = small\n-a to change to Ammount of bytes to Write!")
    print("-append (Appends the Keys to the existing Files) or -write (Delets all existing Characters / Data in File and replaces it with the new Keys) to change the Override Type ( Standart Override is -write (Delets all the Content already in the File)")
    print("Usage ([Word-Cracker.py -d [WordFile] (-a) ([Ammount])")
    


def BreakFile(SelType, FilePath, Ammount):  #Methode to Break the File
    if(CustomOverride):
        if(OverrideFile == False):            
            f = open(FilePath, "a")
            i1 = 0
            msg = ""
            if(isOp == False):
                msg = TEMPLATE #Message at the Top of the File ( Will be Generatet without the OP File )
            
            while(i1 < Ammount):
                msg += KEYS[random.randrange(0, len(KEYS))]
                i1 = i1 + 1
            f.write(msg)
            f.close()
        else:
            f = open(FilePath, "w")
            i2 = 0
            msg = ""
            if(isOp == False):
                msg = TEMPLATE  #Message at the Top of the File ( Will be Generatet without the OP File )
            
            while(i2 < Ammount):
                msg += KEYS[random.randrange(0, len(KEYS))]
                i2 = i2 + 1
            f.write(msg)
            f.close()
    else:
        f = open(FilePath, "w")
        i3 = 0
        msg = ""
        if(isOp == False):
            msg = TEMPLATE + "\n\n"  #Message at the Top of the File ( Will be Generatet without the OP File )
        while(i3 < Ammount):
            msg += KEYS[random.randrange(0, len(KEYS))]
            i3 = i3 + 1
        f.write(msg)
        f.close()
        
    
 #   Check For Custom Bytes ammount
try:    
    USER_KEY3 = sys.argv[3]
    if(USER_KEY3 == "-a"):
        OverrideBytes = True
except:
    pass


try:
    USER_KEY5 = sys.argv[5]
    if(USER_KEY5 == "-append"):
        CustomOverride = True
        OverrideFile = False
    elif(USER_KEY5 == "-write"):
        CustomOverride = True
        OverrideFile = True
    else:
        CustomOverride = False
        
except:
    CustomOverride = False
    pass


#   Check if the User Allowed Bytes Override
try:
    USER_KEY4 = sys.argv[4]
    if(OverrideBytes):
        BytesToWrite = int(USER_KEY4)
except:
    pass


#   Checks for the File Break Type ( and also the OP file Generation )
try:    
    USER_KEY1 = sys.argv[1]
    if(USER_KEY1 == "-d"):
        TypeSelected = "destroy"
        if(OverrideBytes == False):
            BytesToWrite = 1000000
    elif(USER_KEY1 == "-c"):
        TypeSelected = "cracked"
        if(OverrideBytes == False):
            BytesToWrite = 10000
    elif(USER_KEY1 == "-s"):
        TypeSelected = "small"
        if(OverrideBytes == False):
            BytesToWrite = 1000
    elif(USER_KEY1 == "-h"):
        UserHelpDisplay()
    elif(USER_KEY1 == OPKEY):  #Argument to Generate Admin FILE
        print("\nAdmin File Generatet, Launch with op -OP\nIgnore Error Message!!\n")
        GenerateOPFile()
    else:
        print(f"{USER_KEY1} is not a Valid Argument, tpye in Word-Cracker.py -h for help")
        quit()
except:
    print(f"{USER_KEY1} : is an invalid Arguement type -h for help!")
    pass


try:
    #   Import the File to Break and Save the Path to Word File Path
    USER_KEY2 = sys.argv[2]
    if(USER_KEY2 != ""):
        WordFilePath = CURR_FILE_PATH + "\\" + USER_KEY2
        if(os.path.exists(WordFilePath)):
            print("Breaking File, Loading...")
            BreakFile(TypeSelected, WordFilePath, BytesToWrite)
        else:
            print(f"{WordFilePath} does not exist")
    else:
        print("Must Input a Valid File type in -h for Help")
except:
    print("Wrong Argument Usage type in -h for help")
