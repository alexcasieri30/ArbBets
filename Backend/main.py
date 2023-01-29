from Backend.Fanduel.FanduelNFL import FanduelNFL
from Backend.Fanduel.FanduelTableTennis import FanduelTableTennis
from Backend.DraftKings.DraftKingsTableTennis import DraftKingsTableTennis
from Backend.DraftKings.DraftKingsNFL import DraftKingsNFL

executable_path = "/users/alecasie1/desktop/arbbets/chromedriver"

items = [FanduelNFL, FanduelTableTennis, DraftKingsTableTennis, DraftKingsNFL]
# items = [DraftKingsNFL]

# removed pycache
if __name__ == "__main__":
    for item in items:
        startup = item(executable_path)
        startup.run()

