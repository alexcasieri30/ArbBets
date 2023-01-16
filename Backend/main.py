from Fanduel.FanduelNFL import FanduelNFL
from Fanduel.FanduelTableTennis import FanduelTableTennis


executable_path = "/users/alecasie1/desktop/arb/chromedriver"

items = [FanduelNFL, FanduelTableTennis]

if __name__ == "__main__":
    for item in items:
        startup = item(executable_path)
        startup.run()