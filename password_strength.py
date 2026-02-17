def level(score):
    if score > 6:
        return("strong")
    elif score < 6 :
        return ("weak")
    else:
        return("medium")

def strength(password):
    score=0
    if len(password)>=8:
        score+=2
    if (any(c.isdigit() for c in password)):
        score+=2
    if (any (c.isupper() for c in password)):
        score+=2
    if (any(c.islower() for c in password)):
        score+=2
    if (any(c in "!@#$%^&*()-_=+[{]}|;:',<.>/?`~" for c in password)):
        score+=2
    print (f"strength of password is {score} and level {level(score)}")

password=input("enter the password: ")
strength(password)

    
