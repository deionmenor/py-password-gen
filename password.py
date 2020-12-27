import csv
import random

def generateMemorablePassword():
    fh = open("data/word_bank.csv", "r")
    wordReader = csv.reader(fh)
    wordList = []

    for word in wordReader:
        wordList.append(word)
        
    password = random.sample(wordList, k=4)
    password = [p[0] for p in password]
    password = "-".join(password)
    return password

def generateRandomPassword():
    import random
    import string
 
    pwd = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(15))
    return pwd


def generatePassword(p):
    password = ""
    pwd_type = int(p)

    if pwd_type == 1:
        password = generateRandomPassword()
    elif pwd_type ==  2:
        password = generateMemorablePassword()
    else:
        print('Invalid type, generating Random Password by default')
        password = generateRandomPassword()
    return password


while True:
    x = input("Hi! Do you want a new secure password?\n")
    
    if x == "Yes":
        pwd_type = input("(1) Random or (2) memorable?\n")
        print(generatePassword(pwd_type))
        break

    elif x == "No":
        print("Okay then. Your loss.")
        break
