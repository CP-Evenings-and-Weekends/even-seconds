# Imports the datetime class for system clock
# Time module to pause the loop
from datetime import datetime
import time
# outer decorator function.
def only_even_seconds(func):
    # inner wrapper function
    def wrapper(*args, **kwargs):
        # current live clock that grabs current second as a whole number.
        current_second = datetime.now().second
        #checks if the second is even number. 
        if current_second % 2 == 0:

            return func(*args, **kwargs)
        
    return wrapper

# Decorator shortcut stamp.
@only_even_seconds
def shout(message):
    print(message.upper())


for _ in range(10):
    shout("hello!")
    time.sleep(1)