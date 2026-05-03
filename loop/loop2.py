l=["Aman","Ashish","Vishal","Rahul","Aryan"]
#print name that start with "A"
for i in l:
    if(i.startswith("A")):
          print(f"good morning {i}.")

print("Item in list :")
p=0
while (p<len(l)):
     print(l[p])
     p+=1

# print("Item in list :")
# for i in l:
#     print(i)

n= int(input("Enter Number:"))
# sum of n natural number 
i=1
sum=0
while (i<=n):
      sum+=i
      i+=1
print("sum:",sum)  

print("---Facotrial---")
f=1
while(i<=n):
    f*=i
    i+=1
print("Factorial:",f)    

