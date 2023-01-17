from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Backend.ArbTemplate import ArbTemplate

from JSONParser import JSONParser
import uuid
import time
import os
import base64
import json
from threading import Thread

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Last I checked this was necessary.


class DraftKingsTableTennis(ArbTemplate):
    def __init__(self, executable_path, headless=True):
        self.data = {}
        if headless:
            self.driver = webdriver.Chrome(executable_path, chrome_options=options)
        else:
            self.driver = webdriver.Chrome(executable_path)
        self.url = "https://sportsbook.draftkings.com/leagues/tabletennis/tt-elite-series"
        self.sport = "TableTennis"
        self.book = "DraftKings"

    def get_data_snapshot(self):
        els = self.driver.find_element(By.XPATH, '//*[@id="root"]/section/section[2]/section/div[3]/div/div[2]/div/div/div[2]/div/div[2]')
        divs = els.find_elements(By.XPATH, "*")
        for div in divs:
            list_data = div.text.split("\n")
            print(list_data)
            player1 = list_data[3]
            player2 = list_data[5]
            player1odds = list_data[4]
            player2odds = list_data[6]
            ascii_bytes = (player1 + player2).encode('ascii')
            base64_bytes = base64.b64encode(ascii_bytes)
            new_id = base64_bytes.decode('ascii')
            new_id = "DRAFTKINGS-TABLETENNIS-" + new_id[:12]
            newentry = {player1:player1odds, player2:player2odds}
            self.data[new_id] = newentry

