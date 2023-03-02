from typing import List


class Stack:
    def __init__(self):
        self.data: List[str] = []

    def push(self, element: str) -> None:
        self.data.append(element)

    def pop(self) -> str:
        return self.data.pop()

    def top(self) -> str:
        return self.data[-1]

    def is_empty(self) -> bool:
        if self.data:   # if len(self.data) > 0:
            return False
        else:   # elif len(self.data) == 0:
            return True

    # def is_empty(self) -> bool:
    #     return len(self.data) == 0

    def __str__(self) -> str:
        return f"[{', '.join(self.data[::-1])}]"
