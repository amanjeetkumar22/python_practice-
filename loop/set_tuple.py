l=["aman","kalwar","gupta","byahut",3.14,3,]
print("---List Element---")
for i in l:
    print(i)

t=(1,1,2,3,"aman")
i =0
print("---Tuple Element---")
while(i<len(t)):
    print(t[i])
    i+=1

s={1,2,3,4,5,5}
# print(type(s))
print("---Sets Element---")
for i in s:
    print(i)

n="Amanjeet"
print("---String Element---")
for i in n:
    print(i)
else: # if items end in loop then else part execute 
    print("Done:")

