from datetime import datetime
# import time

def only_even_seconds(func):

    def wrapper(message):

        current_second = datetime.now().second

        if current_second % 2 == 0:
            return func(message)

    return wrapper


@only_even_seconds
def shout(message):
    print(message.upper())


shout("hello!")

# for _ in range(10):
#     shout("hello!")
#     time.sleep(1)