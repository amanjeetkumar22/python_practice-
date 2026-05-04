"""
snake =1
water=-1
gun=0
"""
import random

computer=random.choice([1,-1,0])

yournum=input("Enter your choice{s,w,g}:")

dict ={"s": 1, "w": -1, "g":0}

revdict={1:"Snake",-1:"Water",0:"Gun"}

you=dict[yournum]

print(f"you choose: {revdict[you]}\nComputer choose: {revdict[computer]}")

if(computer==you):
    print("Draw:")
else:
    if(computer==-1 and you==1):
        print("You Win.")   
    elif(computer==-1 and you==0):
        print("You loose.")   
    elif(computer==1 and you==-1):
        print("You Loose.")   
    elif(computer==1 and you==0):
        print("You Win.")   
    elif(computer==0 and you==-1):
        print("You Win.")   
    elif(computer==0 and you==1):
        print("You loose.")   


