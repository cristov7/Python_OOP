def vowels(text):
    vowels_list = ["A", "E", "I", "U", "Y", "O"]
    for char in text:
        if char.upper() in vowels_list:
            yield char
        else:
            continue


# my_string = vowels('Abcedifuty0o')
# for char in my_string:
#     print(char)


# def vowels(text):
#     vowels_list = ["A", "E", "I", "U", "Y", "O"]
#     return (char for char in text if char.upper() in vowels_list)
#
#
# my_string = vowels('Abcedifuty0o')
# for char in my_string:
#     print(char)


# from typing import List
#
#
# class vowels:
#     def __init__(self, text: str):
#         self.text = text
#
#     @property  # getter
#     def vowels(self) -> List[str]:
#         vowels_list: List[str] = ["A", "E", "I", "O", "U", "Y"]
#         return vowels_list
#
#     def __iter__(self):
#         return (char for char in self.text if char.upper() in self.vowels)
#
#
# my_string = vowels('Abcedifuty0o')
# for char in my_string:
#     print(char)


# from typing import List
#
#
# class vowels:
#     vowels_list: List[str] = ["A", "E", "I", "O", "U", "Y"]
#
#     def __init__(self, text: str):
#         self.text = text
#         self.__index: int = -1
#         self.__length_text: int = len(self.text)   # self.text.__len__()
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while True:
#             self.__index += 1
#             if self.__index < self.__length_text:
#                 char = self.text[self.__index]
#                 if char.upper() in self.vowels_list:
#                     return char
#                 else:
#                     continue
#             else:
#                 raise StopIteration
#
#
# my_string = vowels('Abcedifuty0o')
# for char in my_string:
#     print(char)
