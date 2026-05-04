p1="Aman"
p2="college"
p3="jata"
p4="nhi"

n=(input("Enter a sentence:"))
#in also works on list 
#p1.lower ->can change the input string in lower case 
if((p1 in n)or(p2 in n)):
    print("Yes found")
else:
    print("Not found")    
