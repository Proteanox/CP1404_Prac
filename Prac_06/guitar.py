"""The main guitar class program"""


class Guitar: # class identifier statement
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self): # str statement for returning output
        return f"{self.name} {self.year} : {self.cost}"

    def get_age(self): # function to check age of guitar
        YEAR = 2020 # end date
        year_diff = YEAR - self.year
        return year_diff

    def is_vintage(self): # function utilising the same pattern to check whether the guitar is vintage or else
        YEAR = 2020
        year_diff = YEAR - self.year
        return year_diff >= 50
