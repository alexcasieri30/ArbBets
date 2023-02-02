from JSONParser import JSONParser
from collections import defaultdict
from DataParser import DataParser
from Helpers import cross_compare


class NFLData(DataParser):
    def __init__(self, data):
        self.data = self.construct_arb_table(data)
        self.arb_data = None

    def construct_arb_table(self, data):
        games = []
        for game_data_across_books in zip(*data):
            all_books = game_data_across_books
            game_event = {}
            for book in all_books:
                for game_data in data:
                    if book in game_data:
                        game_event[book] = game_data[book]
            games.append(game_event)
        return games

    def find_arbs(self):
        for game in self.data:
            if cross_compare(game)==1:
                print("ARB: ", game)