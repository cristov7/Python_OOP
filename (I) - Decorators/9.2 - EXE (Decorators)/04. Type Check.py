def type_check(type_of_arg):   # type_of_arg = parameter from @decorator
    def decorator(function):   # function = func name
        def wrapper(arg):      # arg = args from func name
            if isinstance(arg, type_of_arg):
                result = function(arg)
                return result
            else:
                return "Bad Type"
        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num*2


# print(times2(2))
# print(times2('Not A Number'))


@type_check(str)
def first_letter(word):
    return word[0]


# print(first_letter('Hello World'))
# print(first_letter(['Not', 'A', 'String']))
