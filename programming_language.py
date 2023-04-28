class ProgrammingLanguage:

    def __init__(self, field = "", typing = "", dynamic = True, year = 2000):
        self.field = field
        self.typing = typing
        self.dynamic = dynamic
        self.year = year

    def is_dynamic(self):
        if self.dynamic:
            return True
        else:
            return False

    def __str__(self):
        return ("{}, {} typing, Reflection = {}, First appeared in {}".format(self.field, self.typing, self.dynamic, self.year))