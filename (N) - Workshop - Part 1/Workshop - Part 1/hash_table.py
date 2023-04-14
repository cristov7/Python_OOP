from typing import List


class HashTable:
    def __init__(self):
        self.__max_capacity: int = 4
        self.__keys: List[None] = [None for key in range(self.__max_capacity)]
        self.__values: List[None] = [None] * self.__max_capacity

    def __getitem__(self, key):
        try:
            index = self.__keys.index(key)
            return self.__values[index]
        except ValueError:
            raise KeyError(f"{key} is not a valid key!")

    def __setitem__(self, key, value):
        if key in self.__keys:
            index = self.__keys.index(key)
            self.__values[index] = value
            return
        if len(self) == self.__max_capacity:
            self.__resize()
        index = self.__calc_index(key)
        index = self.__get_index(index)
        self.__keys[index] = key
        self.__values[index] = value

    def __calc_index(self, key: str):
        return sum(ord(char) for char in key) % self.__max_capacity

    def __get_index(self, index: int):
        if index == self.__max_capacity:
            index = 0
        if self.__keys[index] is None:
            return index
        else:
            return self.__get_index(index + 1)

    def __resize(self):
        self.__keys = self.__keys + [None for key in range(self.__max_capacity)]
        self.__values = self.__values + [None] * self.__max_capacity
        self.__max_capacity *= 2

    def __len__(self):
        return len([key for key in self.__keys if key is not None])

    def add(self, key: str, value: str):
        self[key] = value

    def get(self, key: str, default: str = None):
        try:
            return self[key]
        except KeyError:
            return default

    def get_representation(self):
        print("{", end="")
        for i in range(self.__max_capacity):
            key = self.__keys[i]
            if key is not None:
                print(f"{key}: {self.__values[i]},", end=" ")
        print("}")
