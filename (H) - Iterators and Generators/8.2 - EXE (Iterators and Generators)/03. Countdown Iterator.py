class countdown_iterator:
    def __init__(self, count: int):
        self.count = count
        self.__iterations: int = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.__iterations += 1
        if self.__iterations > self.count:
            raise StopIteration
        else:
            number = self.count - self.__iterations
            return number


# iterator = countdown_iterator(10)
# for item in iterator:
#     print(item, end=" ")


# class countdown_iterator:
#     def __init__(self, count: int):
#         self.count = count
#         self.__iterations: int = -1
#
#     def __iter__(self):
#         return (number for number in range(self.count, -1, - 1))
#
#
# iterator = countdown_iterator(10)
# for item in iterator:
#     print(item, end=" ")


# def countdown_iterator(number):
#     for num in range(number, -1, - 1):
#         yield num
#
#
# iterator = countdown_iterator(10)
# for item in iterator:
#     print(item, end=" ")


# def countdown_iterator(number):
#     return (num for num in range(number, -1, - 1))
#
#
# iterator = countdown_iterator(10)
# for item in iterator:
#     print(item, end=" ")
