marks=[]

for i in range(3):
    n=int(input(f"Enter student marks in subject{i+1} :"))
    marks.append(n)
    if n >=33:
        print(f"Student has passed in subject{i+1} :")
    else:
       print(f"Student has failed in subject{i+1} :")    
       break;

print(marks)    
t=sum(marks)
p=(100*(t/300))
if(p>40):
    print("Student Has pass the exam:",p) 
else:
    print("Failed",p)
