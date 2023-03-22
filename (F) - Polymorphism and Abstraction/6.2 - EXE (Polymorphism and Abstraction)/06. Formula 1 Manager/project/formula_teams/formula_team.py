from abc import ABC, abstractmethod
from typing import Dict


class FormulaTeam(ABC):
    def __init__(self, budget: int):
        self.budget = budget

    @property   # getter
    @abstractmethod
    def sponsors(self) -> Dict[str, Dict[int, int]]:
        pass

    @property   # getter
    @abstractmethod
    def expenses(self) -> int:
        pass

    @property   # getter
    def budget(self) -> int:
        return self.__budget

    @budget.setter   # setter
    def budget(self, value) -> [Exception, None]:
        if value < 1_000_000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        else:
            self.__budget = value

    def calculate_revenue_after_race(self, race_pos: int) -> str:
        revenue = 0
        for sponsor_name, sponsor_info_dict in self.sponsors.items():
            for position_place, earned_money in sponsor_info_dict.items():
                if race_pos <= position_place:
                    revenue += earned_money
                    break
                else:
                    continue
        total_revenue = revenue - self.expenses
        self.budget += total_revenue
        current_budget = self.budget
        return f"The revenue after the race is {total_revenue}$. Current budget {current_budget}$"
