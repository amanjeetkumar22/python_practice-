import random

n = random.randint(1,100)

a=-1
guess=0
while(a!=n):
    a=int(input("Enter your guess:-"))
    if(a<n):
        print("Enter higher number")
    
    else:
        print("Enter lower number")
    
    guess+=1

print(f"you guess the number in {guess} attempt that is {n}")