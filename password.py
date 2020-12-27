
def generateMemorablePassword():
    # do something
    return ""

def generateRandomPassword():
    # do something
    return ""


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
