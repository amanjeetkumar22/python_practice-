def sumof(*args):
    for i in args:
        print(i)
    return sum(args)

print("sum is:",sumof(1,2,3,4))