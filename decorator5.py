# Write @require_auth that checks a fake login flag and raises if false 
from functools import wraps
IS_LOGGED_IN = False

def authtic(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if not IS_LOGGED_IN:
            raise PermissionError("Acces denined")
        
        return func(*args,**kwargs)
    return wrapper

@authtic
def get_user_profile():
    return "profile loaded succesfully"

try:
    print(get_user_profile)
except PermissionError as e:
    print(f"error caught: {e}")

IS_LOGGED_IN = True
print(get_user_profile())