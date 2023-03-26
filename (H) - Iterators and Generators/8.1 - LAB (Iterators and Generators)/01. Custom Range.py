class custom_range:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.__number: int = self.start - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.__number += 1
        if self.__number <= self.end:
            current_number = self.__number
            return current_number
        else:
            raise StopIteration


# one_to_ten = custom_range(1, 10)
# for num in one_to_ten:
#     print(num)


# class custom_range:
#     def __init__(self, start: int, end: int):
#         self.start = start
#         self.end = end
#
#     def __iter__(self):
#         return (number for number in range(self.start, self.end + 1))
#
#
# one_to_ten = custom_range(1, 10)
# for num in one_to_ten:
#     print(num)


# def custom_range(start, end):
#     for number in range(start, end + 1):
#         yield number
#
#
# one_to_ten = custom_range(1, 10)
# for num in one_to_ten:
#     print(num)


# def custom_range(start, end):
#     return (number for number in range(start, end + 1))
#
#
# one_to_ten = custom_range(1, 10)
# for num in one_to_ten:
#     print(num)
