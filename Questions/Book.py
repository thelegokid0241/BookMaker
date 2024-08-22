class Book:
    def __init__(self, title, insides ,number):
        self.title = title
        self.insides = insides
        self.number = number

    def __repr__(self):
        return str(self.__dict__)
