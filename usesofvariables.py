t=(input("Enter the Number:"))
b=int (input("Enter the Number:"))

print(type(t))
a=int(t)#type casting
a-=2
print("value of after assining a-=2:",a)

print(f"Sum of {a},{b} is:",a+b)
print(f"remainder of {a},{b} is:",a%b)
print(f"Average of {a},{b} is:",(a+b)/2)
print(f"Square of {b} is:",b**2)

print("a>b",a>b)


print("not(false) means:",not(False))