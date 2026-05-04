a=[]
n=int(input("enter size of input:"))
       

i=0
for i in range(n):
    num=input(f"Enter name {i+1}:")
    a.append(num)

# def fun1(name):
#     # print("Good morning "+name +" Thanks")
#     print(f"Good morning, {name} ")

def fun1(name):
    c="Good morning "+name +" Thanks"
    return c

# print (a) 
for i in a:
   b= fun1 (i) # function with argument 
   print(b) # run after return statement 


# print (a) 
# for i in a:
#     fun1 (i)
    # print(b)

def greet(name,ending="Thanks"):
    print(f"Good morning {name} {ending} ") #if there is not value then it takes its default value 


greet("Aman")
greet ("Amit","Thank you ") #defalt value 

# n=int(input("enter  number :"))
# i=1
# f=1
# while(i<=n):
#     f*=i
#     i+=1

# print(f)

print("--Factorial--")
def fact(f): # function defination 
    if(f==0 or f==1):
        return 1
    return f*fact(f-1)
    
c=fact(n)#function call 
print(c)  

f=3.142857142857
print(round(f,3))#round at three digit 