def number_increment(numbers):   # numbers = [1, 2, 3]
    def increase():
        increment_list = [num + 1
                          for num in numbers]
        return increment_list
    return increase()


# print(number_increment([1, 2, 3]))


# def increment_decorator(function):   # function = func name = number_increment
#     def increase(numbers_list):      # numbers_list = [1, 2, 3]
#         increase_numbers_list = [num + 1 for num in numbers_list]
#         return function(increase_numbers_list)   # function(increase_numbers_list) = number_increment(increase_numbers_list)
#     return increase
#
#
# @increment_decorator
# def number_increment(numbers):
#     return numbers
#
#
# # print(number_increment([1, 2, 3]))   # number_increment([1, 2, 3]) = increase([1, 2, 3])
