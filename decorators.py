import time
# This is the decorator function
def only_even_seconds(func):
    def wrapper(*args, **kwargs):       # will check tome first before running func
        if time.localtime().tm_sec             # checks if seconds are even 
        return
    return wrapper                      # returns the new function

@only_even_seconds # This is the decorator
def greeting():
    # time.sleep(2) *This is not it
    print("Welcome! Enjoy your stay!")
    
greeting()


'''
*** Notes for myself ***

wrapper
    is a function that wraps around the origional function, adding extra 
    behavior before or after calling it. 
    (The name is conventional, it can be called anything)
    
(func)
    is saying it expects to receive a function as in input.
        ex. greeting = even_seconds_only(greeting)
    even seconds will be called w/(greeting) as it's argument
    func is the function you decorated being passed in like any normal value.
    (The name is also conventional)

*args and **kwargs
    Let you write functions that accept any number of arguments without
    knowing in advance how many there will be.    
*args
    positional argument (an argument that's identified by its position 
    (order) rather than it's name).
    *   packs any extra positional argumnets into a tuple.
**kwargs
    keyword arguments (when you pass a value into a function by explicitly
    naming which parameter it belongs to).
    **  packs any extra keyword arguments into a dict.
        A dict can be unpacked with ** back into keyword arguments.

time
    is a module, a collection of functions  *import time* is just importing 
    the module not time itself.
localtime()
    is a function that lives inside the *time* module.
        tm_year=2026,
        tm_mon=6,
        tm_mday=16,
        tm_hour=14,
        tm_min=32,
        tm_sec=42, 
        tm_wday=1,
        tm_yday=167,
        tm_isdst=0
tm_sec
    is a fixed attribute name that Python's localtime() function returns.
sleep()
    pauses your program for a given number of seconds before continuing.

'''