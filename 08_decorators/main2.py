def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with arguments {args} and key arguments {kwargs}")
        result = func(*args, **kwargs)
        print(f"The function {func.__name__} returned {result}")
        return result
    return wrapper

@log_function_call
def add(a,b):
    return a + b

@log_function_call
def greet(name = "Guest"):
    return f"Hello, {name}"

add(2,2)
greet(name="Tauhid")