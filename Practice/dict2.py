a={}

for i in range(4):
    name=input("Enter your name:")
    lan=input(f"Enter language of'{name}':")
    a[name]=lan

a.update({name:lan})#if u want to update your language 
print(a)    