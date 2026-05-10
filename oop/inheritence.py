class student:
    a=1
class std(student):
    b=2

class s(std,student):
    c=3

o=s()
print(o.a,o.b,o.)