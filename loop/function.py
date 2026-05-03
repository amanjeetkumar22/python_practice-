# a=[]
# n=int(input("enter size of input:"))
       

# i=0
# for i in range(n):
#     num=input(f"Enter name {i+1}:")
#     a.append(num)

# def fun1(name):
#     # print("Good morning "+name +" Thanks")
#     print(f"Good morning, {name} ")

# # def fun1(name):
# #     c="Good morning "+name +" Thanks"
# #     return c

# # print (a) 
# # for i in a:
# #    b= fun1 (i)
# #    print(b)


# print (a) 
# for i in a:
#     fun1 (i)
#     # print(b)

n=int(input("enter size of input:"))
# i=1
# f=1
# while(i<=n):
#     f*=i
#     i+=1

# print(f)

def fact(f):
    if(f==0 or f==1):
        return 1
    return f*fact(f-1)
    
c=fact(n)
print(c)    