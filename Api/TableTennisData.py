from JSONParser import JSONParser
from DataParser import DataParser
from collections import defaultdict

class TableTennisData(DataParser):
    def __init__(self, data):
        self.data = self.construct_arb_table(data)
        self.arb_data = None
    
    def construct_arb_table(self, data):
        newdata = defaultdict(list)
        for i, book in enumerate(data):
            for key in book:
                keydata = key.split("-")
                base64key = keydata[2]
                value_obj = {keydata[0]: book[key]}
                newdata[base64key].append(value_obj)
        return newdata

    # this logic should work for every time we see a format with 2 players
    def find_arbs(self):
        for key in self.data:
            if len(self.data[key])>1:
                # multiple books have bets available for the same match
                max_p1 = float("-inf")
                max_p2 = float("-inf")
                lowest_negative_p1 = float("-inf")
                lowest_negative_p2 = float("-inf")
                p1_key = list(list(self.data[key][0].values())[0].keys())[0]
                p2_key = list(list(self.data[key][0].values())[0].keys())[1]
                for book in self.data[key]:
                    max_p1 = max(max_p1, eval(list(book.values())[0][p1_key]))
                    max_p2 = max(max_p2, eval(list(book.values())[0][p2_key]))
                    if eval(list(book.values())[0][p1_key])<0:
                        lowest_negative_p1 = max(lowest_negative_p1, eval(list(book.values())[0][p1_key]))
                    if eval(list(book.values())[0][p2_key])<0:
                        lowest_negative_p2 = max(lowest_negative_p2, eval(list(book.values())[0][p2_key]))
                if (max_p1>0 and max_p2>0):
                    print("ARB: ", self.data[key])
                if (abs(max_p1)>abs(lowest_negative_p2)):
                    print("ARB: ", self.data[key])
                if (abs(max_p2)>abs(lowest_negative_p1)):
                    print("ARB: " , self.data[key])
