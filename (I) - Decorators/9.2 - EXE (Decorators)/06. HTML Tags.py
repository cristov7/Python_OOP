def tags(tag):                 # tag = parameter from @decorator
    def decorator(function):   # function = func name
        def wrapper(*args):    # *args = args from func name
            result = function(*args)
            output = f"<{tag}>{result}</{tag}>"
            return output
        return wrapper
    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)


# print(join_strings("Hello", " you!"))


@tags('h1')
def to_upper(text):
    return text.upper()


# print(to_upper('hello'))
