from datetime import datetime

def only_even_seconds(func):
    def wrapper(*args, **kwargs):
        if datetime.now().second % 2 == 0:
            return func(*args, **kwargs)
        else:
            pass
    return wrapper

@only_even_seconds
def greet(name):
    return f"Howdy, {name}! Welcome to Code Platoon."

message = greet("Steph")
print(message)