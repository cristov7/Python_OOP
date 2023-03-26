def reverse_text(text):
    for char in reversed(text):
        yield char


# for char in reverse_text("step"):
#     print(char, end='')


# def reverse_text(text):
#     return (char for char in reversed(text))
#
#
# for char in reverse_text("step"):
#     print(char, end='')


# class reverse_text:
#     def __init__(self, text: str):
#         self.text = text
#
#     def __iter__(self):
#         return (char for char in reversed(self.text))
#
#
# for char in reverse_text("step"):
#     print(char, end='')


# class reverse_text:
#     def __init__(self, text: str):
#         self.text = text
#         self.__index: int = len(self.text)   # self.text.__len__()
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.__index -= 1
#         if 0 <= self.__index:
#             char = self.text[self.__index]
#             return char
#         else:
#             raise StopIteration
#
#
# for char in reverse_text("step"):
#     print(char, end='')
