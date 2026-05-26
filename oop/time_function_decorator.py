import time

def timer(fun):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fun(*args, **kwargs)
        end = time.time()
        print(f"{fun.__name__} ran in {end-start} time")
        return result
    return wrapper

@timer
def example_function(n):
    time.sleep(n)

example_function(2)

@timer
def addd(a,b):
    time.sleep(4)
    return a+b;

print(addd(2,3))