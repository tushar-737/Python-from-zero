import random

def game():
    print("You are playing a game")
    score=random.randint(1,100)
    with open("hiscore.txt","r") as f:
        hiscore=f.read()
        if hiscore=='':
            hiscore=0
        else:
            hiscore=int(hiscore)
    print(f'''Your score is {score}''')
    if score>hiscore:   
       print("Congratulations! You have the highest score.")
    with open("hiscore.txt","w") as f:
        f.write(str(score))
    return score
game()

