class Time:
    max_hours: int = 23
    max_minutes: int = 59
    max_seconds: int = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, new_hours: int, new_minutes: int, new_seconds: int) -> None:
        self.hours = new_hours
        self.minutes = new_minutes
        self.seconds = new_seconds

    def get_time(self) -> str:
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
        # return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    # def get_time(self) -> str:
    #     hh = f"0{self.hours}" if self.hours < 10 else self.hours
    #     mm = f"0{self.minutes}" if self.minutes < 10 else self.minutes
    #     ss = f"0{self.seconds}" if self.seconds < 10 else self.seconds
    #     return f"{hh}:{mm}:{ss}"

    def next_second(self) -> str:
        if self.seconds + 1 <= Time.max_seconds:
            self.seconds += 1
            return self.get_time()
        else:
            self.seconds = 0
            if self.minutes + 1 <= Time.max_minutes:
                self.minutes += 1
                return self.get_time()
            else:
                self.minutes = 0
                if self.hours + 1 <= Time.max_hours:
                    self.hours += 1
                    return self.get_time()
                else:
                    self.hours = 0
                    return self.get_time()
                    # return "00:00:00"

    # def next_second(self) -> str:
    #     self.seconds += 1
    #     self.update_valid_time()
    #     return self.get_time()
    #
    # def update_valid_time(self) -> None:
    #     if self.seconds > Time.max_seconds:
    #         self.seconds = 0
    #         self.minutes += 1
    #         if self.minutes > Time.max_minutes:
    #             self.minutes = 0
    #             self.hours += 1
    #             if self.hours > Time.max_hours:
    #                 self.hours = 0
