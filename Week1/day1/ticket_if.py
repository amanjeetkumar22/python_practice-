
age=int(input("Enter age:"))
day=input("Enter day:")
nday=day.lower()
if (nday=="wednesday"):
    price= 10 if age >= 18 else 6
else:
    price= 12 if age >= 18 else 8
print(price)