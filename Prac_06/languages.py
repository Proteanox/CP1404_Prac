from Prac_06.programming_language import ProgrammingLanguage


def language():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [ruby, python, visual_basic]

    for i in languages:
        if i.is_dynamic():
            print(i.name)
