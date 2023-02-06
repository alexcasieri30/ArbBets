from Backend.Fanduel.FanduelNFL import FanduelNFL
from Backend.Fanduel.FanduelTableTennis import FanduelTableTennis
from Backend.DraftKings.DraftKingsTableTennis import DraftKingsTableTennis
from Backend.DraftKings.DraftKingsNFL import DraftKingsNFL
from Backend.FoxBet.FoxBetCBB import FoxBetCBB
from Backend.Fanduel.FanduelCBB import FanduelCBB
from Backend.DraftKings.DraftKingsCBB import DraftKingsCBB
executable_path = "/users/alecasie1/desktop/arbbets/chromedriver"

# items = [FanduelNFL, FanduelTableTennis, DraftKingsTableTennis, DraftKingsNFL, FoxBetCBB, FanduelCBB, DraftKingsCBB]
items = [DraftKingsCBB, FoxBetCBB, FanduelCBB]

# removed pycache
if __name__ == "__main__":
    for item in items:
        startup = item(executable_path)
        startup.run()

