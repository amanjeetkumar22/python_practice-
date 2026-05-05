import random 
def game():
    print("You are playing game:")
    score= random.randint(1,100)

    with open("highscore.txt") as f:
        high=f.read()
        if(high!=""):
            high=int(high)
        else:
            high=0   

    print(f"your score:{score}")
    if(score>high):
        with open ("highscore.txt","w") as f:
            f.write(str(score))

    return score 

game()              