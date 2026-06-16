from datetime import datetime

# decor function
# get current time
# is seconds even?
# true execute wrapper
# false do nothing



def only_even_seconds(func):
    def wrapper(*args, **kwargs):
        real_clock = datetime.now().strftime("%H:%M:%S")
        if datetime.now().second % 2 == 0:
            print(f"Landed on even number! Current time: {real_clock}") 
            return func(real_clock, *args, **kwargs) 
        
        else: 
            return None
    return wrapper  
 
@only_even_seconds
def current_time(accurate_time):
    print(f"This exact moment ({accurate_time}) is an even number in seconds.")

current_time()