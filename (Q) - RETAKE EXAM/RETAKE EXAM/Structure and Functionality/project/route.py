class Route:
    def __init__(self, start_point: str, end_point: str, length: float, route_id: int):
        self.start_point = start_point   # the start point of the route
        self.end_point = end_point       # the end point of the route
        self.length = length             # the length of the route in kilometers
        self.route_id = route_id         # the id of the route
        self.is_locked: bool = False     # the status of the route

    @property   # getter
    def start_point(self) -> str:
        return self.__start_point

    @start_point.setter   # setter
    def start_point(self, value: str) -> [ValueError, None]:
        if value == "" or value.isspace():
            raise ValueError("Start point cannot be empty!")
        else:
            self.__start_point = value

    @property   # getter
    def end_point(self) -> str:
        return self.__end_point

    @end_point.setter   # setter
    def end_point(self, value: str) -> [ValueError, None]:
        if value == "" or value.isspace():
            raise ValueError("End point cannot be empty!")
        else:
            self.__end_point = value

    @property   # getter
    def length(self) -> float:
        return self.__length

    @length.setter   # setter
    def length(self, value: float) -> [ValueError, None]:
        if value < 1.00:
            raise ValueError("Length cannot be less than 1.00 kilometer!")
        else:
            self.__length = value
