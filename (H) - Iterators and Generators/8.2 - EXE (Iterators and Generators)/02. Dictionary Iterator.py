from typing import List, Tuple


class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dictionary = dictionary
        self.__list_with_tuples: List[Tuple] = list(self.dictionary.items())

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.__list_with_tuples) > 0:   # if self.__list_with_tuples.__len__():
            current_tuple = self.__list_with_tuples.pop(0)
            return current_tuple
        else:
            raise StopIteration


# result = dictionary_iter({1: "1", 2: "2"})
# for x in result:
#     print(x)


# class dictionary_iter:
#     def __init__(self, dictionary: dict):
#         self.dictionary = dictionary
#
#     def __iter__(self):
#         return ((key, value) for (key, value) in self.dictionary.items())
#
#
# result = dictionary_iter({1: "1", 2: "2"})
# for x in result:
#     print(x)


# def dictionary_iter(dictionary):
#     for key, value in dictionary.items():
#         current_tuple = (key, value)
#         yield current_tuple
#
#
# result = dictionary_iter({1: "1", 2: "2"})
# for x in result:
#     print(x)


# def dictionary_iter(dictionary):
#     return ((key, value) for (key, value) in dictionary.items())
#
#
# result = dictionary_iter({1: "1", 2: "2"})
# for x in result:
#     print(x)
