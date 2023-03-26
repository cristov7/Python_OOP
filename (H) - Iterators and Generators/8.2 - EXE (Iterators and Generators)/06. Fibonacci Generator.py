def fibonacci():
    first_number = 0
    second_number = 1
    yield first_number
    yield second_number
    while True:
        number = first_number + second_number
        yield number
        first_number = second_number
        second_number = number


# generator = fibonacci()
# for i in range(5):
#     print(next(generator))


# def fibonacci():
#     first_number = 0
#     second_number = 1
#     while True:
#         yield first_number
#         first_number, second_number = second_number, first_number + second_number
#
#
# generator = fibonacci()
# for i in range(5):
#     print(next(generator))
