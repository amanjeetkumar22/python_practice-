s="amanjeet"

r=""

for i in s:
    r=i+r
for i in s:##first non repeated character  
    if s.count(i)==1:
        print("yes this is first charcter:",i)
        break
print(r)