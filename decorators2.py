# create a decorator to print the fuction name and the values of the arguments every time the function is called 

# this is kind of most basic decorator 
# def debug(func):
#     def wrapper(*args, **kwargs):
#        return func(*args, *kwargs)

#     return wrapper


def debug(func):
    def wrapper(*args, **kwargs):
       args_value = ' ,'.join(str(arg) for arg in args ) # this we are working with arguments 
       kwargs_value =', '. join (f"{k}={v}" for k ,v in kwargs.items()) # this is we are working with k value pairs 
       print(f"calling {func.__name__} with args {args_value} and kwargs {kwargs_value}")
       return func(*args, *kwargs)

    return wrapper


@debug
def greet(name,greeting ="good morning"):
    print(f"{greeting} , {name}")


greet("sparsh","namaste")