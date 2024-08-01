def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('something is happening before function is called')
        func(*args, **kwargs)
        print('something is happening after the function is called')
    return wrapper

@my_decorator
def say_hello(a, b):
    print('Hello!', a, b)

say_hello(5, 4)

