print("---list---")
list =["Aman","grapes","roomate",89,89.98,"3B"]
list[4]=90
list.append("room") # to add something in last 
print("1.After the updating list",list)
list.reverse()
print("2.reversing of list:",list) #it takes updated value 
print("3. type of your data:",type(list))
print("4.to print the 4th item of list ",list[4])

a="Aman"
print("5.to print the  a[2] of Aman",a[2])

l=[] #to create empty list 
print("6. l[] empty list",type(l))

l=[1,2,"aman",8.96,9.0,9]

print("7. using loop")
for i in l:
    print(i)


# tupple parts 
print("---Tupple---")
t=("aman",32,38.888,"am")

# t[2]=38 # 'tuple' object does not support item assignment
print("8.tuple element",t)
print("9. accessing t[2]",t[2])

b=(2,0,3,0,4,5,0)

print("10.sum",sum(b))

print("11.occurance of b:",b.count(0))

# n=b.count(0) #method2 to count the digit 
# print(n)

t1=() #to create empty tupple 
print("12.empty tuple t=():",type(t1))
t1=("aman",9.0,8,9)
print("13.element of tuple:")
for i in t1:
    print(i)


