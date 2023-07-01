class CustomList:
    def __init__(self):
        self.custom_list: list = []

    def append(self, value) -> list:
        self.custom_list.append(value)
        return self.custom_list

    def remove(self, index: int):
        try:
            value = self.custom_list[index]
            self.custom_list.remove(value)
            return value
        except IndexError:
            raise IndexError(f"'{index}' is invalid index!")

    def get(self, index: int):
        try:
            value = self.custom_list[index]
            return value
        except IndexError:
            raise IndexError(f"'{index}' is invalid index!")

    def extend(self, iterable) -> list:
        iterable_list = list(iterable)
        self.custom_list.extend(iterable_list)
        return self.custom_list

    def insert(self, index: int, value) -> list:
        self.custom_list.insert(index, value)
        return self.custom_list

    def pop(self):
        try:
            value = self.custom_list.pop()
            return value
        except IndexError:
            raise IndexError("Can't pop from empty list!")

    def clear(self) -> None:
        self.custom_list.clear()

    def index(self, value) -> [int, ValueError]:
        try:
            index = self.custom_list.index(value)
            return index
        except ValueError:
            raise ValueError(f"'{value}' is not in list!")

    def count(self, value) -> int:
        count = self.custom_list.count(value)
        return count

    def reverse(self) -> list:
        self.custom_list.reverse()
        return self.custom_list

    def copy(self) -> list:
        new_custom_list = CustomList()
        new_custom_list.custom_list = self.custom_list.copy()
        return new_custom_list.custom_list

    def size(self) -> int:
        size = len(self.custom_list)
        return size

    def add_first(self, value) -> None:
        self.custom_list.insert(0, value)

    def dictionize(self) -> dict:
        key_list = [self.custom_list[index] for index in range(len(self.custom_list)) if index % 2 == 0]
        value_list = [self.custom_list[index] for index in range(len(self.custom_list)) if index % 2]
        if len(key_list) > len(value_list):
            value_list.append(" ")
        custom_dict = dict(zip(key_list, value_list))
        return custom_dict

    def move(self, amount: int) -> [list, IndexError]:
        if 0 < amount < len(self.custom_list):
            amount_list = self.custom_list[:amount]
            self.custom_list = self.custom_list[amount:] + amount_list
            return self.custom_list
        else:
            raise IndexError(f"'{amount}' is invalid amount!")

    def sum(self) -> [int, float]:
        sum_of_the_list = 0
        for element in self.custom_list:
            if isinstance(element, int) or isinstance(element, float):
                sum_of_the_list += element
            else:
                sum_of_the_list += len(str(element))
        return sum_of_the_list

    def overbound(self) -> [int, Exception]:
        if self.custom_list:
            index = 0
            biggest_value = None
            for element_index, element in enumerate(self.custom_list):
                if not isinstance(element, (int, float)):
                    element = len(str(element))
                if biggest_value is None or element > biggest_value:
                    biggest_value = element
                    index = element_index
                else:
                    continue
            return index
        else:
            raise Exception("Can't return index from an empty list!")

    def underbound(self) -> [int, Exception]:
        if self.custom_list:
            index = 0
            smallest_value = None
            for element_index, element in enumerate(self.custom_list):
                if not isinstance(element, (int, float)):
                    element = len(str(element))
                if smallest_value is None or element < smallest_value:
                    smallest_value = element
                    index = element_index
                else:
                    continue
            return index
        else:
            raise Exception("Can't return index from an empty list!")

    def is_empty(self) -> bool:
        return len(self.custom_list) == 0

    def remove_all_occurrences(self, value) -> list:
        self.custom_list = [element for element in self.custom_list if element != value]
        return self.custom_list
