class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} {self.year} : {self.cost}"

    def get_age(self):
        YEAR = 2020
        year_diff = YEAR - self.year
        return year_diff

    def is_vintage(self):
        YEAR = 2020
        year_diff = YEAR - self.year
        return year_diff >= 50

