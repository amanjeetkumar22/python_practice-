t=float(input("Enter the temperature:"))

def conv(t):
    F=((t*1.8) + 32)
    return F


print("temp. in fernheit is =",conv(t))