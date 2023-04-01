from project.delicacies.delicacy import Delicacy


class Stolen(Delicacy):
    @property   # getter
    def get_portion(self) -> int:   # implemented method
        portion = 250   # grams
        return portion

    def __init__(self, name: str, price: float):
        super().__init__(name, self.get_portion, price)
