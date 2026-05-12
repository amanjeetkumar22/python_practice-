class student:
    name="Amit"
    room ="89"
    floor="3"

    def getinfo(self):#when u introduce any method then use "self" to  call 
        print(f"room  is : {self.room}, and floor is :{self.floor}")
    
    @staticmethod
    def greet():
        print(f"good morning {student.name}")
    
    @classmethod##it takes only class attributes value 
    def getinfoclass(cls):#when u introduce any method then use "cls" to  call 
        print(f"branch is : {cls.room}, and campus is :{cls.floor}")

    @property ##u can return after using property 
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

o=student()
# # print(o.greet)
# o.getinfo()
# o.greet()
# o.getinfoclass()

o.name="Aman Jeet"
print(o.name)
print(o.fname,o.lname)