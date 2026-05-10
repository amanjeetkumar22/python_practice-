from random import randint

class Train:
    def __init__(self,trainno):
        self.trainno=trainno

    def book(self,fro,to):
        print(f"your train no { self.trainno} is booked from {fro} to {to} ")

    def getstatus(self):
        print(f"your seat is booked in train number {self.trainno}")

    def getfare(self,fro,to):
        print(f"your train no {self.trainno} is booked from {fro} to {to} and ticket fair is {randint(222,5555)}")    

p=Train("19270")

p.book("nke","lko")
p.getstatus()
p.getfare("nke","lko")
