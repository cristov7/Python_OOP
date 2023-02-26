class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0

    def fill(self, ml: int) -> str:
        if self.content + ml <= Glass.capacity:   # Glass.capacity == self.capacity
            self.content += ml
            return f"Glass filled with {ml} ml"
        else:
            return f"Cannot add {ml} ml"

    def empty(self) -> str:
        self.content = 0
        return "Glass is now empty"

    def info(self) -> str:
        space_left = Glass.capacity - self.content   # Glass.capacity == self.capacity
        return f"{space_left} ml left"


# glass = Glass()
# print(glass.fill(100))
# print(glass.fill(200))
# print(glass.empty())
# print(glass.fill(200))
# print(glass.info())
