def generatePassword(answer):
    print("password123")

while True:
    x = input("Hi! Do you want a new secure password?\n")
    
    if x == "Yes":
        generatePassword(x)
        break

    elif x == "No":
        print("Okay then. Your loss.")
        break
