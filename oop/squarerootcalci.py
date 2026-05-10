class cal:

    def __init__(self,n):
        self.n=n

    def squareroot(self):
        print(f"Squareroot is:{self.n**0.5}")

    def square(self):
        print(f"square={self.n*self.n}")

    def cube(self):
        print(f"square={self.n*self.n*self.n}")

c=cal(4)

c.squareroot() 
c.square()
c.cube()      