# # Liskov Substitution (LSP):


from abc import ABC, abstractmethod


class Duck(ABC):
    @abstractmethod
    def quack(self):
        pass

    @abstractmethod
    def walk(self):
        pass

    @abstractmethod
    def fly(self):
        pass


class RubberDuck(Duck):
    def quack(self) -> str:
        return "Squeek"

    def walk(self) -> Exception:
        """Rubber duck can walk only if you move it"""
        raise NotImplementedError('I cannot walk by myself')

    def fly(self) -> Exception:
        """Rubber duck can fly only if you throw it"""
        raise NotImplementedError('I cannot fly by myself')


class RobotDuck(Duck):
    HEIGHT: int = 50

    def __init__(self):
        self.height: int = 0

    def quack(self) -> str:
        return 'Robotic quacking'

    def walk(self) -> str:
        return 'Robotic walking'

    def fly(self) -> None:
        """can only fly to specific height but
        when it reaches it starts landing automatically"""
        if self.height == RobotDuck.HEIGHT:
            self.land()
        else:
            self.height += 1

    def land(self) -> None:
        self.height = 0
