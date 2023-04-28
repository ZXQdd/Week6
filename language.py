from prac_06.programming_language import ProgrammingLanguage

def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    java = ProgrammingLanguage("Java", "Static", False, 1995)

    print(python)

    languages = [ruby, python, visual_basic, java]
    print("The dynamic typed languages are: ")
    for language in languages:
        if language.is_dynamic():
            print(language.field)


main()