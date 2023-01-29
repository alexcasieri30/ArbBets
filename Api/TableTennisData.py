from JSONParser import JSONParser

class TableTennisData:
    def __init__(self, data):
        self.data = data

    def print_data(self):
        d = JSONParser(self.data)
        d.pretty_print()