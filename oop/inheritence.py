class student:
    a=1

class stud:
    h=3
class std(student,stud):##multiple inheritance 
    b=2

class s(std,student):#multilevel inheritance
    c=3

##multiple inheritance
k=std()
print(k.h,k.a,k.b)

##multilevel inheritance 
o=student()
print(o.a)#output->1 

o=std()
print(o.a,o.b)#output->1 2 

o=s()
# print(o.a,o.b,o.c) #output->1 2 3 