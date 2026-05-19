def even(n):
    for i in range(2,n+1,2):
        # print(i)
        # return i
        yield i ##store memory location and refrence (state) ## yield number generator 
for num in even(10):
    print(num)
    # print(even(10))