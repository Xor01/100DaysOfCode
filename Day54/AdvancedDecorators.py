def logging_decorator(function):
    def wrapper(*args):
        print(f"You called {function.__name__} {args}")
        print("It returned: ", function(*args))
    return wrapper


@logging_decorator
def printMe(a, b):
    return a+b


printMe(1,2)
