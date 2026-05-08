n = 5
num = 1

for i in range(1, n + 1):
    
    for j in range(i):
        
        if num % 2 == 0:
            print("*", end=" ")
        else:
            print(num, end=" ")
        
        num += 1
    
    print()