n = 5
num = 1

for i in range(1, n + 1):

    for j in range(i):

        # Check prime
        is_prime = True

        if num < 2:
            is_prime = False
        else:
            for k in range(2, int(num ** 0.5) + 1):
                if num % k == 0:
                    is_prime = False
                    break

        # Output logic
        if is_prime and num % 5 == 0:
            print("PF", end=" ")

        elif is_prime:
            print("P", end=" ")

        elif num % 5 == 0:
            print("F", end=" ")

        else:
            print(num, end=" ")

        num += 1

    print()