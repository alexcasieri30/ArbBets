import json
from NFLData import NFLData
from TableTennisData import TableTennisData
import time


BOOKS = ["DraftKings", "Fanduel"]
SPORTS = ["NFL", "TableTennis"]

while True:
    for sport in SPORTS:
        all_sport_data = {}
        sport_data = []
        for book in BOOKS:
            with open("/users/alecasie1/desktop/ArbBets/Backend/Data/{}/{}.json".format(book, sport), 'r') as f:
                data = json.load(f)
                sport_data.append(data)
        if sport == "NFL":
            all_sport_data[sport] = NFLData(sport_data)
        elif sport == "TableTennis":
            all_sport_data[sport] = TableTennisData(sport_data)
        # all_sport_data[sport].print_data()
        try:
            all_sport_data[sport].find_arbs()
        except Exception as e:
            print("ERROR: ", e)
            continue
    time.sleep(10)

