def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice
    
    
def do_twice_args(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice