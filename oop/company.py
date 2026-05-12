class Programmer:
    company="Microsoft"

    def __init__(self,name,dep,salary):
        self.name=name
        self.dep=dep
        self.salary=salary

        
nu=int(input("Number of client:"))
programmers=[]
for i in range(nu):
    n=input("Enter Name:")
    d=input("Enter department:")
    s=input("Salary:")
    p=Programmer(n,d,s)
    programmers.append(p)

for i in programmers:##how to store all data and print 
    print(i.name,i.dep,i.salary,i.company)

