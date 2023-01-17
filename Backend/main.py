from Fanduel.FanduelNFL import FanduelNFL
from Fanduel.FanduelTableTennis import FanduelTableTennis
from DraftKings.DraftKingsTableTennis import DraftKingsTableTennis

executable_path = "/users/alecasie1/desktop/arb/chromedriver"

items = [FanduelNFL, FanduelTableTennis, DraftKingsTableTennis]
# items = [DraftKingsTableTennis]

if __name__ == "__main__":
    for item in items:
        startup = item(executable_path)
        startup.run()