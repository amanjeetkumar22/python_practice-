t=(input("Enter the Number:")) #always take input as string 
b=int (input("Enter the Number:"))
i=3.4
print(type(i)) #return float 
print(type(t))
a=int(t)#type casting
a-=2 #decrement a value by 2 and assign in a 
print("value of after assining a-=2:",a)

print(f"Sum of {a},{b} is:",a+b)
print(f"remainder of {a},{b} is:",a%b)
print(f"Average of {a},{b} is:",(a+b)/2)
print(f"Square of {b} is:",b**2)
print(f"floor division //",a//b) # return only integer value 

print("a>b",a>b)#return true and false value 


print("not(false) means:",not(False)) #print true 