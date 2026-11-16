# clouser 

def outter_function(msg):
    def inner_function():
        print(f"this is inner function {msg}")
    return inner_function  #this is closure




# we need to find the execution time of the function 

import time
def execution_time(func):
    def wapper(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wapper

@execution_time
def timmer(n):
    time.sleep(n)

timmer(2)



# decorator ka simple systax is like fuction as another fuction and the fuction passed through that previous function x