from calendar import month_name


class DVD:
    def __init__(self, name: str, dvd_id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = dvd_id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented: bool = False

    @classmethod
    def from_date(cls, dvd_id: int, name: str, date: str, age_registration: int):
        creation_day, creation_month, creation_year = map(int, date.split("."))   # "day.month.year"
        return cls(name, dvd_id, creation_year, month_name[creation_month], age_registration)

    def __repr__(self) -> str:
        dvd_id = self.id
        dvd_name = self.name
        creation_month = self.creation_month
        creation_year = self.creation_year
        age_registration = self.age_restriction
        status = "rented" if self.is_rented else "not rented"
        return f"{dvd_id}: {dvd_name} ({creation_month} {creation_year}) has age restriction {age_registration}. Status: {status}"
