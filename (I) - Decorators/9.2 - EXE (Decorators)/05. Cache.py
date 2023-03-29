def cache(func):        # func = func name
    def wrapper(arg):   # arg = args from func name
        if arg in wrapper.log.keys():
            return wrapper.log[arg]
        else:
            value = func(arg)
            wrapper.log[arg] = value
            return wrapper.log[arg]
    wrapper.log = {}
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# fibonacci(3)
# print(fibonacci.log)
