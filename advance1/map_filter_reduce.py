from functools import reduce
##map
l=[1,2,3,4,5,6,7]

sqr= lambda x : x*x

sqrlist=map(sqr,l)

print(list(sqrlist))

##filter

even=lambda y:y%2==0

evenn=filter(even,l)
print(list(evenn))

##reduce 
def sum(a,b):
    return a+b
mul=lambda x,y:x*y
print(l)
print(f"sum is :{reduce(sum,l)}")
# print(f"multiply  is :{reduce(mul,l)}")
print("multiply  is :",reduce(mul,l))
