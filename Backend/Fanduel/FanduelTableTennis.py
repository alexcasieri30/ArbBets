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


class FanduelTableTennis(ArbTemplate):
    def __init__(self, executable_path, headless=True):
        self.data = {}
        if headless:
            self.driver = webdriver.Chrome(executable_path, chrome_options=options)
        else:
            self.driver = webdriver.Chrome(executable_path)
        self.url = "https://sportsbook.fanduel.com/table-tennis"
        self.sport = "TableTennis"
        self.book = "Fanduel"

    def get_data_snapshot(self):
        ul = self.driver.find_element(By.XPATH, '//*[@id="main"]/div/div[1]/div/div/div[2]/div[2]/ul')
        lis = ul.find_elements(By.XPATH, "*")
        for li in lis:
            list_data = li.text.split("\n")
            if len(list_data)==6:
                player1 = list_data[0]
                player1odds = list_data[2]
                player2 = list_data[1]
                player2odds = list_data[3]
                ascii_bytes = ''.join(set(player1 + player2)).encode('ascii')
                base64_bytes = base64.b64encode(ascii_bytes)
                new_id = base64_bytes.decode('ascii')
                new_id = "FANDUEL-TABLETENNIS-" + new_id
                newentry = {player1:player1odds, player2:player2odds}
                self.data[new_id] = newentry

