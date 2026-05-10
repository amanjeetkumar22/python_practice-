class student :
    branch= "cse" #class attribute 
    # name="Amon"
    camp = "25"

    def getinfo(self):#when u introduce any method then use "self" to  call 
        print(f"branch is : {self.branch}, and campus is :{self.camp}")
    
    # def greet(r):##anything can be used to call its a variable 
    #     print("Good Morning")

    @staticmethod #decorator ## no need of object 
    def greet():
        print("Good Morning")

aman = student() #object-> aman
aman.name="Aman" #instance/ object attribute 

print(aman.name,aman.branch,aman.camp)

aman.getinfo()#TypeError: student.getinfo() takes 0 positional arguments but 1 was given
##student.getinfo(aman) this means 
aman.greet()