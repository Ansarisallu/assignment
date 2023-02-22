import random
def gamewin(you,comp):
    if comp==you:
        return None
    elif comp=='s':
        if you=='g':
            return True
        elif you=='w':
            return False
    elif comp=='w':
        if you=='s':
            return True
        elif you=='g':
            return False
    elif comp=='g':
        if you=='w':
            return True
        elif you=='s':
            return False

print("computer turn:snake(s),water(w),gun(g)")
ranno=random.randint(1, 3)
if ranno==1:
    comp='s'
elif ranno==2:
    comp='w'
elif ranno==3:
    comp='g'



you=input("your turn snake(s),water(w),gun(g)")

a=gamewin(you,comp)

print(f"computer chose :{comp}")
print(f"you are chose :{you}")


if a==None:
    print("Game tie")
elif a:
    print("your are winner")
else:
    print("you are loser")