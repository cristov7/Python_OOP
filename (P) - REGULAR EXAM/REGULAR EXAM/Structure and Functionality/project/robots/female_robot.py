from project.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):
    ROBOT_KG: int = 7

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, self.ROBOT_KG)

    @property                           # getter
    def increase_weight(self) -> int:   # implemented method
        increase_kg = 1
        return increase_kg
