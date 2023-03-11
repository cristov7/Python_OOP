class Room:
    def __init__(self, number: int, capacity: int):
        self.number = number
        self.capacity = capacity
        self.guests: int = 0
        self.is_taken: bool = False

    def take_room(self, people: int) -> [None, str]:
        if not self.is_taken:
            if people <= self.capacity:
                self.is_taken = True
                self.guests = people
            else:
                number = self.number
                return f"Room number {number} cannot be taken"
        else:
            number = self.number
            return f"Room number {number} cannot be taken"

    def free_room(self):
        if self.is_taken:
            self.is_taken = False
            self.guests = 0
        else:
            number = self.number
            return f"Room number {number} is not taken"
