def even_numbers(function):   # function = func name = get_numbers
    def wrapper(numbers):     # numbers = args from func name = [1, 2, 3, 4, 5]
        numbers_list = function(numbers)
        even_numbers_list = [number for number in numbers_list
                             if number % 2 == 0]
        return even_numbers_list
    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


# print(get_numbers([1, 2, 3, 4, 5]))


# def even_numbers(function):   # function = func name = get_numbers
#     def wrapper(numbers):     # numbers = arguments from func name = [1, 2, 3, 4, 5]
#         even_numbers_list = [number for number in numbers
#                              if number % 2 == 0]
#         return even_numbers_list
#     return wrapper
#
#
# @even_numbers
# def get_numbers(numbers):
#     return numbers
#
#
# # print(get_numbers([1, 2, 3, 4, 5]))
