c1=complex(1,2)
c2=complex(3,4)
class complex:
    def __init__(self,r,i):
        self.r=r
        self.i=i

    def __add__(self,c2):
        # return complex(self.r+c2.r,self.i+c2.i)   ##show object address 
        return f"{self.r+c2.r}+{self.i+c2.i}i"   

    # def __str__(self):##define printing format 
    #     return f"{self.r}+{self.i}i"
    
print(c1+c2)