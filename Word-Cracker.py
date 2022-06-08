import os
import os.path
import sys
import random


KEYS_BIG = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
KEYS_SMALL = "abcdefghijklmnopqrstuvwxyz"
KEYS_NUMBERS = "1234567890"
KEYS = KEYS_BIG + KEYS_SMALL + KEYS_NUMBERS #Full Keys


CURR_FILE_PATH = __file__.replace("\Word-Cracker.py", "")


OP_FILENAME = "\MKCRACKER.OOPP" #Generatet OP FileName
isOp = False


OverrideBytes = False   #If True the Bytes to Write can be Overriten
hasADKey = False        #ADKey = Admin Key = Opperator Permissions
TypesToCrypt = ["destroy", "cracked", "small"]  #All The Types of Breaking
TypeSelected = ""
WordFilePath = ""
BytesToWrite = 100000   #Can be Overriten if OverrideBytes = True


def GenerateOPFile():   #Generates the OP File if User Input Argument is Correct
    f = open(CURR_FILE_PATH + OP_FILENAME, "w")
    f.write("Admin Key!")
    f.close()


def UserHelpDisplay(): #Display User Help with all Commands
    print("Word-Cracker Arguments :\n-d = Destroy\n-c = Cracked\n-s = small\n-a to change to Ammount of bytes to Write!")
    print()
    print("Usage ([Word-Cracker.py -d [WordFile] (-a) ([Ammount])")
    


def BreakFile(SelType, FilePath, Ammount):  #Methode to Break the File
    f = open(FilePath, "w")
    i = 0
    msg = ""
    if(isOp == False):
        msg = "!!!FILE CRACKED WITH MK CRACKER!!!"  #Message at the Top of the File ( Will be Generatet without the OP File )
    
    while(i < Ammount):
        msg += KEYS[random.randrange(0, len(KEYS))]
        i = i + 1
    f.write(msg)
    f.close()

    
 #   Check for Admin File Key
try:    
    USER_KEY3 = sys.argv[3]
    if(USER_KEY3 == "-OP"):
        if(os.path.exists(CURR_FILE_PATH + OP_FILENAME)):
            isOp = True
            print("Opperator Permissions loaded!")
        else:
            print("-OP is not a Valid Argument!")
    elif(USER_KEY3 == "-a"):
        OverrideBytes = True
except:
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
    elif(USER_KEY1 == "--Generate.Admin.File#MK"):  #Argument to Generate Admin FILE
        print("\nAdmin File Generatet, Launch with op -OP\nIgnore Error Message!!\n")
        GenerateOPFile()
    else:
        print(f"{USER_KEY1} is not a Valid Argument, tpye in Word-Cracker.py -h for help")
        quit()
    
    
    #   Import the File to Break and Save the Path to Word File Path
    USER_KEY2 = sys.argv[2]
    if(USER_KEY2 != ""):
        WordFilePath = CURR_FILE_PATH + USER_KEY2
        if(os.path.exists(WordFilePath)):
            print(WordFilePath)
            BreakFile(TypeSelected, WordFilePath, BytesToWrite)
        else:
            print(f"{WordFilePath} does not exist")
    else:
        print("Must Input a Valid File type in -h for Help")
except:
    print("Wrong Argument Usage type in -h for help")
