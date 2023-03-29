def logged(function):       # function = func name
    def wrapper(*args):     # *args = args from func name
        name_of_function = function.__name__
        parameters = ", ".join([str(arg) for arg in args])
        result_of_the_execution = function(*args)
        output = "\n".join([f"you called {name_of_function}({parameters})",
                            f"it returned {result_of_the_execution}"])
        return output
    return wrapper


@logged
def func(*args):
    return 3 + len(args)


# print(func(4, 4, 4))


@logged
def sum_func(a, b):
    return a + b


# print(sum_func(1, 4))
