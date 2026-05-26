def debug(fun):
    def wrapper(*args,**kwargs):
        args_value=', '.join(str(arg) for arg in args)
        kwargs_value=', '.join(f"{k}={v}" for k,v in kwargs.items())
        print(f"calling:{fun.__name__} with args {args_value} and kwargs {kwargs_value}")
        return fun(*args, **kwargs)
    return wrapper

@debug ## to pass from the debug function 
def hello():
    print("Hello")

@debug ## to pass from the debug function 
def greet(name,greeting="Hello Sir"):
    print(f"{greeting},{name}")

hello()
greet("Aman",greeting="good sir")