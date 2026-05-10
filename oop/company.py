class Programmer:
    company="Microsoft"

    def __init__(self,name,dep,salary):
        self.name=name
        self.dep=dep
        self.salary=salary

        
nu=int(input("Number of client:"))

for i in range(1,nu):
    n=input("Enter Name:")
    d=input("Enter department:")
    s=input("Salary:")
    p=Programmer(n,d,s)

for i in range(1,nu):##how to store all data and print 
    print(p.name,p.dep,p.salary,p.company)