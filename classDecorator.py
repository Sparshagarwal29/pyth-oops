# insted of using the fuction deco we can use class decorator 

# 1. class base decorator without argument 
from functools import update_wrapper
from typing import Any
class countcall :
    def __init__(self,func) :
        self.func = func
        self.num_call = 0   
    def __call__(self, *args, **kwds):
        pass

def process_data(data):
    return data.strip()