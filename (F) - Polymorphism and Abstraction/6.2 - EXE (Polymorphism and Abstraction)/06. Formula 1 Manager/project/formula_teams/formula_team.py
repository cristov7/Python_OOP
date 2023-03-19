from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    def __init__(self, budget: int):
        self.budget = budget

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < 1_000_000:   # 1000000 == 1_000_000
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        else:
            self.__budget = value

    @property
    @abstractmethod
    def sponsors(self):
        pass

    @property
    @abstractmethod
    def expenses_per_one_race(self):
        pass

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = 0
        for position_dict in self.sponsors.values():   # [{position: money}, {position: money}, ...]
            for position in position_dict.keys():      # [position, position, ...]
                if race_pos <= position:
                    revenue += position_dict[position]
                    break
                else:
                    continue
        revenue -= self.expenses_per_one_race
        self.budget += revenue
        budget = self.budget
        return f"The revenue after the race is {revenue}$. Current budget {budget}$"
