class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.__iterations: int = - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.__iterations += 1
        if self.__iterations == self.count:
            raise StopIteration
        else:
            number = self.__iterations * self.step
            return number


# numbers = take_skip(2, 6)
# for number in numbers:
#     print(number)


# class take_skip:
#     def __init__(self, step: int, count: int):
#         self.step = step
#         self.count = count
#
#     def __iter__(self):
#         return (count_number * self.step
#                 for count_number in range(self.count))
#
#
# numbers = take_skip(2, 6)
# for number in numbers:
#     print(number)


# def take_skip(step, count):
#     for count_number in range(count):
#         yield count_number * step
#
#
# numbers = take_skip(2, 6)
# for number in numbers:
#     print(number)


# def take_skip(step, count):
#     return (count_number * step
#             for count_number in range(count))
#
#
# numbers = take_skip(2, 6)
# for number in numbers:
#     print(number)
