# this is an @retry(times =3) function it makes it compulsory to use nesed wrapper 
# how to read --> a) retry we know we need to use try and exceptoion block ; 
# Level 1 (Outer): Accepts timer=3
# Level 2 (Middle): Accepts func
# Level 3 (Inner): Accepts *args, **kwargs to run the target function


from functools import wraps
import random

def retry(times = 3):
    def decorator(func):
        @wraps(func)
        def wrappper(*args, **kwargs):
            for attempts in range(1, times+1):
                try:
                   return func(*args,**kwargs)
                except Exception as e:
                    print(f"{attempts}/{times} failed : {e}") 
            print("all attempt fail")
            raise
        return wrappper
    return decorator


@retry(times=3)
def api_calling():
    print("api calling")
    if random.random()<0.7:
        raise Exception("server delay")
    return "data fetched succesfully"


api_calling()