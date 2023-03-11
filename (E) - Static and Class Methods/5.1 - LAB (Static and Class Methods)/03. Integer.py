from math import floor


class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value: float):
        if not isinstance(float_value, float):   # if type(float_value) != float:
            return "value is not a float"
        else:
            floor_value = floor(float_value)
            return cls(floor_value)

    @classmethod
    def from_roman(cls, value: str):
        roman_values_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        convert_value = 0
        for index in range(len(value)):
            if index != 0 and roman_values_dict[value[index]] > roman_values_dict[value[index - 1]]:
                convert_value += roman_values_dict[value[index]] - 2 * roman_values_dict[value[index - 1]]
            else:
                convert_value += roman_values_dict[value[index]]
        return cls(convert_value)

    @classmethod
    def from_string(cls, value: str):
        if not isinstance(value, str):   # if type(value) != str:
            return "wrong type"
        else:
            int_value = int(value)
            return cls(int_value)


# first_num = Integer(10)
# print(first_num.value)
#
# second_num = Integer.from_roman("IV")
# print(second_num.value)
#
# print(Integer.from_float("2.6"))
# print(Integer.from_string(2.6))
