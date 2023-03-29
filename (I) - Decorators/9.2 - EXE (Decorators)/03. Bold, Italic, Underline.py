def make_bold(function):   # function = func name
    def wrapper(*args):    # *args = args from func name
        result = function(*args)
        output = f"<b>{result}</b>"
        return output
    return wrapper


def make_italic(function):   # function = func name
    def wrapper(*args):      # *args = args from func name
        result = function(*args)
        output = f"<i>{result}</i>"
        return output
    return wrapper


def make_underline(function):   # function = func name
    def wrapper(*args):         # *args = args from func name
        result = function(*args)
        output = f"<u>{result}</u>"
        return output
    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


# print(greet("Peter"))


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


# print(greet_all("Peter", "George"))
