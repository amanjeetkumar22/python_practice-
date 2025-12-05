greatest = None   # to store the greatest value

for i in range(4):
    num = int(input(f"Enter number {i+1}: "))

    if greatest is None:     # first number becomes greatest
        greatest = num
    elif num > greatest:
        greatest = num       # update greatest

print("The greatest number is:", greatest)
