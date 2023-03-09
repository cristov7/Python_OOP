class Player:
    def __init__(self, name: str, sprint: int, dribble: int, passing: int, shooting: int):
        self.__name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self):
        return self.__name

    def __str__(self) -> str:
        name = self.__name
        sprint = self.__sprint
        dribble = self.__dribble
        passing = self.__passing
        shooting = self.__shooting
        return f"Player: {name}" \
               f"\nSprint: {sprint}" \
               f"\nDribble: {dribble}" \
               f"\nPassing: {passing}" \
               f"\nShooting: {shooting}"
