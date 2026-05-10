class student:
    # name="Aman"
    branch="cse"
    cam="25"
    
    def __init__(self,name,branch,cam):
    # def __init__(self):
        self.name=name
        self.branch=branch
        self.cam=cam
        print("I am an object")

    @staticmethod
    def greet():
        print("Good Evening")

aman=student("Amit","Ai","24") #here we can pass the value 
# aman.greet()
aman.name="Aman"
print(aman.name,aman.branch)