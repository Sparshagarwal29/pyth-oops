#decortor that returns the value  of a function so that when it's called with the same argument the cached value is returned insted of re-exectuting the fuction 


#this kind of show how cache work
import time

def cache(func):
    cache_value = {}
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result 
        return result
    return wrapper 


@cache  
def long_running_function(a,b):
    time.sleep(4)
    return a+b 


print(long_running_function(2,4)) 
print(long_running_function(3,4))
print(long_running_function(2,4)) #this would be printed instantly without any time delay showing cache system properly working 
print(long_running_function(2,2))