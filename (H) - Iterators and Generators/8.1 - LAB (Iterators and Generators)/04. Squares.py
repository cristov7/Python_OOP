def squares(number):
    for num in range(1, number + 1):
        yield num ** 2


# print(list(squares(5)))


# def squares(number):
#     return (num ** 2 for num in range(1, number + 1))
#
#
# print(list(squares(5)))


# class squares:
#     def __init__(self, number: int):
#         self.number = number
#
#     def __iter__(self):
#         return (num ** 2 for num in range(1, self.number + 1))
#
#
# print(list(squares(5)))


# class squares:
#     def __init__(self, number: int):
#         self.number = number
#         self.__counter: int = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.__counter += 1
#         if self.__counter > self.number:
#             raise StopIteration
#         else:
#             square_number = self.__counter ** 2
#             return square_number
#
#
# print(list(squares(5)))
