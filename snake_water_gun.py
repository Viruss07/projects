#  snake drinks water ; water drowns gun ; gun kills snake 
def game():
    import random
    Choice={"snake":1,"water":-1,"gun":0}
    computer=random.choice(list(Choice.keys()))
    you=input("you want to choose \n snake \n gun \n water: \n ")

    print(f"your choice is {you} and computer is {computer}")

    if computer==you:
        print("it's tie")

    else:
        if(computer=="snake" and you=="water"):
            print("computer win")
        elif(computer=="snake"and you=="gun"):
            print("you win")
        elif(computer=="water"and computer=="snake"):
            print("computer win")
        elif(computer=="water"and computer=="gun"):
         print("you win")
        elif(computer=="gun"and you=="snake"):
            print("computer win")
        elif(computer=="gun"and you=="water"):
            print("you win")

a=input("hey wanna play? (yes/no)")
if a =="yes":
    print("here we go")
    game()
else:
    print("okay")