from typing import List


class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __repr__(self) -> str:
        name = self.name
        surname = self.surname
        return f"{name} {surname}"

    def __add__(self, other) -> object:
        name = self.name
        surname = other.surname
        return Person(name, surname)


class Group:
    def __init__(self, name: str, people: List[Person]):
        self.name = name
        self.people = people

    def __len__(self) -> int:
        length_of_a_group = len(self.people)
        return length_of_a_group

    def __add__(self, other) -> object:
        first_name = self.name
        second_name = other.name
        name = f"{first_name} {second_name}"
        people = self.people + other.people
        return Group(name, people)

    def __repr__(self) -> str:
        name = self.name
        members = ", ".join(person.__repr__()
                            for person in self.people)
        return f"Group {name} with members {members}"

    def __getitem__(self, item) -> str:
        index = item
        person = self.people[index].__repr__()
        return f"Person {index}: {person}"
