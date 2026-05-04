a=[]
n=int(input("Enter the size:"))
for i in range (n):
    num=int(input("Enter the numbers:"))
    a.append(num)
print("your input numbers are:-",a)

def greatesst(n):
    
    greatest=n[0]
    
    for i in n:
        if i > greatest:
           greatest=i
           
    return greatest    
    
print("greatest=",greatesst(a)) 