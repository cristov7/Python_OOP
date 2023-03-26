def get_primes(list_of_integer_numbers):
    for number in list_of_integer_numbers:
        if number > 1:
            for divider in range(2, number):
                if number % divider == 0:
                    break
                else:
                    continue
            else:
                yield number
        else:
            continue


# print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))


# import math
#
#
# def get_primes(list_of_integer_numbers):
#     for number in list_of_integer_numbers:
#         if number > 1:
#             for divider in range(2, int(math.sqrt(number)) + 1):
#                 if number % divider == 0:
#                     break
#                 else:
#                     continue
#             else:
#                 yield number
#         else:
#             continue
#
#
# print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
