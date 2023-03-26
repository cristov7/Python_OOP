def read_next(*args):
    for element in args:
        for nested_element in element:
            yield nested_element


# for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
#     print(item, end='')


# def read_next(*args):
#     for element in args:
#         if isinstance(element, str):   # if type(element) == str:
#             for char in element:
#                 yield char
#         elif isinstance(element, tuple):   # elif type(element) == tuple:
#             for tuple_element in element:
#                 yield tuple_element
#         elif isinstance(element, dict):   # elif type(element) == dict:
#             for key_element in element.keys():
#                 yield key_element
#         elif isinstance(element, list):   # elif type(element) == list:
#             for list_element in element:
#                 yield list_element
#         elif isinstance(element, set):   # elif type(element) == set:
#             for set_element in element:
#                 yield set_element
#         else:
#             yield element
#
#
# for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
#     print(item, end='')
