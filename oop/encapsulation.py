class car:
    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model

    def get_brand(self):
        return self.__brand + "!"
    
    def namee(self):
        return f"{self.__brand}-{self.model}"
    
class electric(car):
    def __init__(self,brand,model,battery):
        super().__init__(brand,model)
        self.battery=battery



# c=car("mahindra","jeep")
# print(c.brand)
# print(c.namee())

# e=electric("tesla","model s","8kwh")
# print(e.model)
# print(e.namee())

c=car("mahindra","jeep")
print(c.__brand)
print(c.namee())