from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Backend.ArbTemplate import ArbTemplate

import uuid
import time
import os
import json
import base64
from threading import Thread

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')


class DraftKingsNFL(ArbTemplate):
    def __init__(self, executable_path, headless=True):
        self.data = {}
        if headless:
            self.driver = webdriver.Chrome(executable_path, chrome_options=options)
        else:
            self.driver = webdriver.Chrome(executable_path)
        self.url = "https://sportsbook.draftkings.com/leagues/football/nfl"
        self.sport = "NFL"
        self.book = "DraftKings"

    def get_data_snapshot(self):
        table = self.driver.find_element(By.XPATH, '//*[@id="root"]/section/section[2]/section/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/table/tbody')
        rows = table.find_elements(By.XPATH, "tr")
        event = {}
        event_name = ""
        for i, row in enumerate(rows):
            rowdata = row.find_elements(By.TAG_NAME, "td")
            team = row.find_element(By.TAG_NAME, 'th').find_element(By.TAG_NAME, 'a').find_element(By.CLASS_NAME, 'event-cell').text
            teamdata = []
            try:
                for k, col in enumerate(rowdata):
                    if k == 1:
                        d = col.text.split("\n")
                        ou = d[0] + d[1]
                        n = d[2]
                        teamdata += [ou, n]
                    else:
                        teamdata += [*col.text.split("\n")]
                event[team] = teamdata
                event_name += team
                print(event)
            except Exception as e:
                print(e)
            if i%2==1:
                try:
                    try:
                        ascii_bytes = (event_name).encode('ascii')
                        base64_bytes = base64.b64encode(ascii_bytes)
                        new_id = base64_bytes.decode('ascii')
                    except Exception as e:
                        print(e)
                    print("NEW ID: ", new_id)
                    new_id = "DRAFTKINGS-NFL-" + new_id[:12]
                    print(new_id, event)
                    self.data[new_id] = event
                    print("SELF.DATA: ", self.data)
                    event = {}
                    event_name = ""
                except Exception as e:
                    print("ERROR: ", e)
        print(self.data)
