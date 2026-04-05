import random

def guess():
    n=random.randint(1,100)
    print("You have 5 chances to choose a no. from 1 to 100")
    for i in range (1,6):
        user=int(input(f"Enter {i} number:- "))
        if(user>100):
            print("the input is not in range")
        elif(n==user):
            print("Your guess is correct")
            break        
        elif(n>user):
            print("Answer is high")
        elif(n<user):
            print("Answer is low")
    return        
guess()