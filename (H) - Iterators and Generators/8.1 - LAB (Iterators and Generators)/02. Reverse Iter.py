class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.__index: int = len(self.iterable)   # self.iterable.__len__()

    def __iter__(self):
        return self

    def __next__(self):
        if 0 < self.__index:
            self.__index -= 1
            element = self.iterable[self.__index]
            return element
        else:
            raise StopIteration


# reversed_list = reverse_iter([1, 2, 3, 4])
# for item in reversed_list:
#     print(item)


# class reverse_iter:
#     def __init__(self, iterable):
#         self.iterable = iterable
#
#     def __iter__(self):
#         return (element for element in reversed(self.iterable))
#
#
# reversed_list = reverse_iter([1, 2, 3, 4])
# for item in reversed_list:
#     print(item)


# def reverse_iter(numbers_list):
#     for number in reversed(numbers_list):
#         yield number
#
#
# reversed_list = reverse_iter([1, 2, 3, 4])
# for item in reversed_list:
#     print(item)


# def reverse_iter(numbers_list):
#     return (number for number in reversed(numbers_list))
#
#
# reversed_list = reverse_iter([1, 2, 3, 4])
# for item in reversed_list:
#     print(item)
