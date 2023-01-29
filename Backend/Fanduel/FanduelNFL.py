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


class FanduelNFL(ArbTemplate):
    def __init__(self, executable_path, headless=True):
        self.data = {}
        if headless:
            self.driver = webdriver.Chrome(executable_path, chrome_options=options)
        else:
            self.driver = webdriver.Chrome(executable_path)
        self.url = "https://sportsbook.fanduel.com/navigation/nfl"
        self.sport = "NFL"
        self.book = "Fanduel"

    def get_data_snapshot(self):
        ul = self.driver.find_element(By.XPATH, '//*[@id="main"]/div/div[1]/div/div/div[1]/div/div[3]/ul')
        lis = ul.find_elements(By.XPATH, "*")
        for li in lis:
            list_data = li.text.split("\n")
            if len(list_data)<5:
                continue
            team1 = list_data[0]
            team2 = list_data[1]
            team1moneyline = list_data[4]
            team2moneyline = list_data[9]
            ascii_bytes = (team1 + team2).encode('ascii')
            base64_bytes = base64.b64encode(ascii_bytes)
            new_id = base64_bytes.decode('ascii')
            new_id = "FANDUEL-NFL-" + new_id[:12]
            newentry = {team1:team1moneyline, team2:team2moneyline}
            self.data[new_id] = newentry
