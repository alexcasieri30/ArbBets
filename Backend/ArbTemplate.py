from JSONParser import JSONParser
import json
import os
import time
from threading import Thread


class ArbTemplate:
    def __init__(self):
        self.sport = None
        self.data = {}
        self.driver = None
        self.url = None

    def print_data(self):
        jsondata = JSONParser(self.data)
        jsondata.pretty_print()

    def save(self):
        cwd = os.getcwd()
        with open(cwd + f"/data/Fanduel/{self.sport}.json", 'w') as f:
            json_obj = json.dumps(self.data, indent=4)
            f.write(json_obj)
    
    def run(self, continuous=True):
        print(f"starting {self.sport} thread")
        t1 = Thread(target=self.get_data, args=[continuous])
        t1.start()

    def start(self):
        self.driver.get(self.url)

    def close(self):
        self.driver.quit()

    def get_data_snapshot(self):
        pass

    def get_data_continuous(self):
        while True:
            print("-" * 50)
            print('getting data...')
            self.get_data_snapshot()
            self.print_data()
            self.save()
            print("sleeping")
            time.sleep(10)

    def get_data(self, continuous=True):
        self.start()
        if continuous:
            self.get_data_continuous()
        else:
            self.get_data_snapshot()
        self.close()
