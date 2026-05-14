a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

if(b==0):
    raise ZeroDivisionError("Your program is not meant  to divide by zero")
else:
    print(a/b)

print("success")