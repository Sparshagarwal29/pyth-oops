# itreator : an oject that returns element one at a time from a sequence (or data stream) and remember the position between calls   
# a python object is called itreator is it has :
# a) __iter__() --> return the iterator object itself 
# b) __next__() --> returns the next item in the sequence 
# 

import random
class dice :
    def __init__(self,roll):
        self.roll = roll 
        self.count = 0
    def __iter__(self):  #this just return the fucntion itself 
        return self
    def __next__(self):
        if self.count<self.roll:
            self.count +=1
            return random.randint(1,6)
        else:
            raise StopIteration #we need to use this to stop when no more items 