# # 1. Abstract Factory:


# We are going to create an AbstractFactory class that will have methods for creating chairs, sofas, and tables:


from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_chair(self):
        raise NotImplementedError()

    @abstractmethod
    def create_sofa(self):
        raise NotImplementedError()

    @abstractmethod
    def create_table(self):
        raise NotImplementedError()


# Then we are going to create the Chair, Sofa and Table classes:


class Chair:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Sofa:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Table:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


# Finally, we are going to create three different factories that will inherit from the AbstractFactory class:
# VictorianFactory, ModernFactory, FuturisticFactory


class VictorianFactory(AbstractFactory):
    def create_chair(self):
        return Chair("victorian chair")

    def create_sofa(self):
        return Sofa("victorian sofa")

    def create_table(self):
        return Table("victorian table")


class ModernFactory(AbstractFactory):
    def create_chair(self):
        return Chair("modern chair")

    def create_sofa(self):
        return Sofa("modern sofa")

    def create_table(self):
        return Table("modern table")


class FuturisticFactory(AbstractFactory):
    def create_chair(self):
        return Chair("futuristic chair")

    def create_sofa(self):
        return Sofa("futuristic sofa")

    def create_table(self):
        return Table("futuristic table")
