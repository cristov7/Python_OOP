def multiply(times):           # decorator name(times to run)
    def decorator(function):   # decorator(func name)
        def wrapper(number):   # wrapper(args from func name)
            add_number = function(number)
            multiply_result = add_number * times
            return multiply_result
        return wrapper
    return decorator


@multiply(3)
def add_ten(number):
    return number + 10


# print(add_ten(3))


# def multiply(times):           # decorator name(times to run)
#     def decorator(function):   # decorator(func name)
#         def wrapper(number):   # wrapper(args from func name)
#             result = 0
#             for _ in range(times):
#                 result += function(number)
#             return result
#         return wrapper
#     return decorator
#
#
# @multiply(3)
# def add_ten(number):
#     return number + 10
#
#
# # print(add_ten(3))
