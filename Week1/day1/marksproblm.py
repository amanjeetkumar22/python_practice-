marks=[] #declaring tuples 

for i in range(3):
    n=int(input(f"Enter student marks in subject{i+1} :"))
    marks.append(n) #append is used to add in end 
    if n >=33: #in each subject need 33% to passed
        print(f"Student has passed in subject{i+1} :")
    else:
       print(f"Student has failed in subject{i+1} :")    
       break; 

print(marks)    
t=sum(marks)
p=(100*(t/300))
if(p>40):#in total subject need 40 % to passed 
    print("Student Has pass the exam:",p) 
else:
    print("Failed",p)
