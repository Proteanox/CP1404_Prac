class ProgrammingLanguage:
    def __init__(self, name="", typing="", reflection="", year=""):
        self.year = year
        self.reflection = reflection
        self.typing = typing
        self.name = name

    def __str__(self):
        return f"{self.name}, Typing: {self.typing} , Reflection: {self.reflection}, in Year: {self.year}"

    def is_dynamic(self):
        return self.typing == "Dynamic"


