from abc import ABC, abstractmethod
from typing import List
from project.robots.base_robot import BaseRobot


class BaseService(ABC):   # AbstractBaseClass
    def __init__(self, name: str, capacity: int):
        self.name = name                    # the name of the service
        self.capacity = capacity            # the number of robots а service can have
        self.robots: List[BaseRobot] = []   # robots (objects) added to the service

    @property   # getter
    def name(self) -> str:
        return self.__name

    @name.setter   # setter
    def name(self, value: str) -> [ValueError, None]:
        if value == "" or value.isspace():
            raise ValueError("Service name cannot be empty!")
        else:
            self.__name = value

    @property   # getter
    def capacity(self) -> int:
        return self.__capacity

    @capacity.setter   # setter
    def capacity(self, value: int) -> [ValueError, None]:
        if value <= 0:
            raise ValueError("Service capacity cannot be less than or equal to 0!")
        else:
            self.__capacity = value

    @abstractmethod             # abstractmethod
    def details(self) -> str:   # must be implemented
        pass
