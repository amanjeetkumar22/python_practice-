import math
def circle(r):
    a=math.pi * (r**2)
    c=2*math.pi*r
    return a,c
a,c=circle(2)
d=round(a,2)
e=round(c,2)
print("area:",d,"Circumference:",e)