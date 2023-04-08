from project.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):
    ROBOT_KG: int = 9

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, self.ROBOT_KG)

    @property                           # getter
    def increase_weight(self) -> int:   # implemented method
        increase_kg = 3
        return increase_kg
