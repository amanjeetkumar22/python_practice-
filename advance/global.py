a=90
# def fun():
#     # global a # it change the global variable value 
#     a=3
#     print("i am fun",a)

# fun()
# print("I am the boss",a) 

# def fun1():
#     a=88
#     def fun2():
#         print("i am fun 2,",a)
#     fun2()
#     fun()
# fun1()
# print("i am the last",a)


# def fun1():
#     a=88
#     def fun2():
#         print("i am fun 2,",a)
#     return fun2
# print("i am the last",a)
# r=fun1()
# r()

def fun3(n):
    def actuall(a):
        return a**n
    return actuall

# def fun3(2):
#     def actuall(a):
#         return a**2
#     return actuall

f=fun3(2)
g=fun3(3)
print("i am 2f,",f(2))
print("i am 3g,",g(3))