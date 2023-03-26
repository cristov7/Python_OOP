class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.__iterations: int = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.__iterations += 1
        if self.__iterations == self.number:
            raise StopIteration
        else:
            index = self.__iterations % len(self.sequence)
            char = self.sequence[index]
            return char


# result = sequence_repeat('abc', 5)
# for item in result:
#     print(item, end='')


# class sequence_repeat:
#     def __init__(self, sequence: str, number: int):
#         self.sequence = sequence
#         self.number = number
#
#     def __iter__(self):
#         return (self.sequence[index] if index < len(self.sequence)
#                 else self.sequence[index % len(self.sequence)]
#                 for index in range(self.number))
#
#
# result = sequence_repeat('abc', 5)
# for item in result:
#     print(item, end='')


# def sequence_repeat(sequence, number):
#     for index in range(number):
#         if index < len(sequence):
#             char = sequence[index]
#             yield char
#         else:
#             index = index % len(sequence)
#             char = sequence[index]
#             yield char
#
#
# result = sequence_repeat('abc', 5)
# for item in result:
#     print(item, end='')


# def sequence_repeat(sequence, number):
#     return (sequence[index] if index < len(sequence)
#             else sequence[index % len(sequence)]
#             for index in range(number))
#
#
# result = sequence_repeat('abc', 5)
# for item in result:
#     print(item, end='')
