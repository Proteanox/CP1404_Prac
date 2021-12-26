""" thE primary class program for programming-languages"""


class ProgrammingLanguage: # Class name and identifier
    def __init__(self, name="", typing="", reflection="", year=""): # defining the init method for input of values
        self.year = year # year parameter
        self.reflection = reflection
        self.typing = typing
        self.name = name

    def __str__(self): # str method for output values
        return f"{self.name}, Typing: {self.typing} , Reflection: {self.reflection}, in Year: {self.year}"

    def is_dynamic(self): # dynamic function for checking the language type
        return self.typing == "Dynamic"
