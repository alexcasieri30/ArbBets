from JSONParser import JSONParser
from collections import defaultdict
from Helpers import cross_compare

BOOKS = ["DraftKings", "Fanduel"]

class DataParser:
    def __init__(self, data):
        self.data = None
        self.arb_data = None

    def print_data(self):
        d = JSONParser(self.data)
        d.pretty_print()