marks=[]
n=int(input("Enter number of student:"))
for i in range(n):
    mark=int(input(f"Enter mark of{i+1} student:"))
    marks.append(mark)
print("Marks of all student:\n",marks)  

marks.sort() #to arrange them in increasing order 

print("Marks after sorting:",marks)

print("Sum of total marks:", sum(marks))