from project.delicacies.delicacy import Delicacy


class Gingerbread(Delicacy):
    @property   # getter
    def get_portion(self) -> int:   # implemented method
        portion = 200   # grams
        return portion

    def __init__(self, name: str, price: float):
        super().__init__(name, self.get_portion, price)
