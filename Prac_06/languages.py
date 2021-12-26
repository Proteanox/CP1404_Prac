"""client program for operation procedure"""


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


def language(): # language function to create the list an perform operations
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [ruby, python, visual_basic]
    print("The dynamic languages are:")
    for i in languages:
        if i.is_dynamic():
            print(i.name)


language()
