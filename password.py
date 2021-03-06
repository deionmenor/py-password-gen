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

def generateRandomPassword(length=15):
    import random
    import string
 
    pwd = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length))
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
    x = input("Hi! Do you want a new secure password?\n(1) Yes\n(2) No\n")
    
    if x == "1":
        try:
            pwd_type = input("Type?\n(1) Random\n(2) Memorable\n")
            print(generatePassword(pwd_type))
            break
        except ValueError:
            print("Don't be stupid. It said 1 or 2.")

    elif x == "2":
        print("Okay then. Your loss\n.")
        break
    else:
        print("Incorrect input.\n")
