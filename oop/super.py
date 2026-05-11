class student:
    def __init__(self):
        print("I am student")
    a=1

class stud:
    h=3
class std(student,stud):##multiple inheritance 
    def __init__(self):
        print("I am std")
    b=2

class s(std,student):#multilevel inheritance
    def __init__(self):
        super().__init__()##to call parent class constructor 
        print("I am s")
    c=3
##multiple inheritance
# k=std()
# print(k.h,k.a,k.b)

##multilevel inheritance 
# o=student()
# print(o.a)

# o=std()
# print(o.a,o.b)

o=s()
print(o.a,o.b,o.c)