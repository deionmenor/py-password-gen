def generatePassword():
    password = "password123"
    return password

while True:
    x = input("Hi! Do you want a new secure password?\n")
    
    if x == "Yes":
        print(generatePassword())
        break

    elif x == "No":
        print("Okay then. Your loss.")
        break
