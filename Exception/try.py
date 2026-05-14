try:
    a=int(input("Enter your number:"))
    print(a)
except ValueError as v:
    print(v)
    print("hii")

except Exception as e:
    print(e)

print("Thank you:")