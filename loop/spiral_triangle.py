n = 5
start = 1

for i in range(1, n + 1):

    num = start

    for j in range(i):
        print(num, end=" ")
        num += 2

    print()

    if i % 2 == 1:
        start += i + 1
    else:
        start += i