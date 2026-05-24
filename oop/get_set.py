class Student:

    def __init__(self):
        self.__marks = 0   # private variable

    # Setter Method
    def set_marks(self, marks):
        self.__marks = marks

    # Getter Method
    def get_marks(self):
        return self.__marks


# Creating object
s1 = Student()

# Setting value
s1.set_marks(95)

# Getting value
print("Marks =", s1.get_marks())