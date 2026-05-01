n=int(input("Enter your number:"))

def sum(n):
    if(n==1):
        return 1   
    else:
        return sum(n-1)+n    
    

print("sum=",sum(n))
