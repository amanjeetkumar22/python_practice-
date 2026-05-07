n = 5
num = 1

for i in range(1, n + 1):
    
    for j in range(i):
        
        if num % 3 == 0:
            print("X", end=" ")
        else:
            print(num, end=" ")
        
        num += 1
    
    print()