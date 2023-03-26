def genrange(start, end):
    for number in range(start, end + 1):
        yield number


# print(list(genrange(1, 10)))


# def genrange(start, end):
#     return (number for number in range(start, end + 1))
#
#
# print(list(genrange(1, 10)))


# class genrange:
#     def __init__(self, start: int, end: int):
#         self.start = start
#         self.end = end
#
#     def __iter__(self):
#         return (number for number in range(self.start, self.end + 1))
#
#
# print(list(genrange(1, 10)))


# class genrange:
#     def __init__(self, start: int, end: int):
#         self.start = start
#         self.end = end
#         self.__number: int = self.start - 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.__number += 1
#         if self.__number <= self.end:
#             number = self.__number
#             return number
#         else:
#             raise StopIteration
#
#
# print(list(genrange(1, 10)))
