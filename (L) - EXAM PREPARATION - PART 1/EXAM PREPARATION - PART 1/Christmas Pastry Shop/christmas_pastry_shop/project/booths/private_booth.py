from project.booths.booth import Booth


class PrivateBooth(Booth):
    @property   # getter
    def get_price_per_person(self) -> float:   # implemented method
        price_per_person = 3.50   # lv
        return price_per_person
