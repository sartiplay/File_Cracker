KEYS_BIG = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
KEYS_SMALL = "abcdefghijklmnopqrstuvwxyz"
KEYS_NUMBERS = "1234567890"
KEYS_SYMBOLS = "}{][/_-.%#*+"
KEYS = KEYS_BIG + KEYS_SMALL + KEYS_SYMBOLS + KEYS_NUMBERS  #Full Keys

OPKEY = "--Generate.Admin.File#MK"

OPKEYIN = "Admin Key : Admin.Key.Generated#1758! "

CURR_FILE_PATH = __file__.replace("\cfg\config.py", "")


OP_FILENAME = "\MKCRACKER.OOPP" #Generatet OP FileName

OPFILEPATH = CURR_FILE_PATH + OP_FILENAME

TEMPLATE= "!!!FILE CRACKED WITH MK CRACKER!!!"


def GenerateOPFile():   #Generates the OP File if User Input Argument is Correct
    f = open(OPFILEPATH, "w")
    f.write(OPKEYIN)
    f.close()