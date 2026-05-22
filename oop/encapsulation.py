class car:
    def __init__(self,brand,model):
        self.__brand=brand#double _ _ is for private 
        self.model=model

    def get_brand(self):##underscore is sign for private(_)
        return self.__brand + "!"
    
    def namee(self):
        return f"{self.__brand}-{self.model}"
    def fuel(self):##polymorphism 
        return "petrol or diesel"
    
class electric(car):
    def __init__(self,brand,model,battery):
        super().__init__(brand,model)
        self.battery=battery
    
    def fuel(self): ##polymorphism 
        return "Electric"
    


c=car("mahindra","jeep")
# print(c.brand)
print(c.namee())
print(c.fuel())##polymorphism 

e=electric("tesla","model s","8kwh")
print(e.model)
print(e.namee())
print(e.fuel())##polymorphism 


# c=car("mahindra","jeep") #encapsulation demo
# print(c.get_brand()) #encapsulation demo
# # print(c.namee())