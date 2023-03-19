from typing import List


class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __repr__(self) -> str:
        return f"{self.name} {self.surname}"

    def __add__(self, other) -> object:
        name = self.name
        surname = other.surname
        new_person = Person(name, surname)
        return new_person


class Group:
    def __init__(self, name: str, people: List[Person]):
        self.name = name
        self.people = people

    def __len__(self) -> int:
        return len(self.people)

    def __add__(self, other) -> object:
        first_name = self.name
        second_name = other.name
        name = f"{first_name} {second_name}"
        people = self.people + other.people
        new_group = Group(name, people)
        return new_group

    def __repr__(self) -> str:
        name = self.name
        members = ", ".join([person.__repr__()
                             for person in self.people])
        return f"Group {name} with members {members}"

    def __getitem__(self, index) -> str:
        person = self.people[index]
        return f"Person {index}: {person}"
