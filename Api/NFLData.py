from JSONParser import JSONParser
from collections import defaultdict

BOOKS = ["DraftKings", "Fanduel"]

class NFLData:
    def __init__(self, data):
        self.data = self.construct_arb_table(data)
        self.arb_data = defaultdict(list)

    def print_data(self):
        d = JSONParser(self.data)
        d.pretty_print()

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
    

def cross_compare(obj):
    key1, key2 = obj.keys()
    book1 = obj[key1]
    book2 = obj[key2]
    book1team1, book1team2 = book1.keys()
    book2team1, book2team2 = book2.keys()
    book1team1spread = eval(book1[book1team1].replace(u'\u2212', '-'))
    book2team2spread = eval(book2[book2team2].replace(u'\u2212', '-'))
    print("OP 1: ", book1team1spread, book2team2spread)
    if book1team1spread>0 and book2team2spread>0:
        return 1
    if book1team1spread*book2team2spread<0:
        if book1team1spread>0 and abs(book1team1spread)>abs(book2team2spread):
            return 1
        if book2team2spread>0 and abs(book2team2spread)>abs(book1team1spread):
            return 1
    book1team2spread =  eval(book1[book1team2].replace(u'\u2212', '-'))
    book2team1spread = eval(book2[book2team1].replace(u'\u2212', '-'))
    print("OP 2: ", book1team2spread, book2team1spread)
    if book1team2spread>0 and book2team1spread>0:
        return 1
    if book1team2spread*book2team1spread<0:
        if book1team2spread>0 and abs(book1team2spread)>abs(book2team1spread):
            return 1
        if book2team1spread>0 and abs(book2team1spread)>abs(book1team2spread):
            return 1
    return -1


