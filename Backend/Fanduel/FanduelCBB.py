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


class FanduelCBB(ArbTemplate):
    def __init__(self, executable_path, headless=True):
        self.data = {}
        if headless:
            self.driver = webdriver.Chrome(executable_path, chrome_options=options)
        else:
            self.driver = webdriver.Chrome(executable_path)
        self.url = "https://sportsbook.fanduel.com/navigation/ncaab"
        self.sport = "CBB"
        self.book = "Fanduel"

    def get_data_snapshot(self):
        uls = self.driver.find_element(By.XPATH, '//*[@id="main"]/div/div[1]/div/div/div[1]/div/div[3]/ul')
        lis = uls.find_elements(By.TAG_NAME, "li")
        for li in lis:
            try:
                inner_div = li.find_element(By.TAG_NAME, "div").find_element(By.TAG_NAME, "div").find_element(By.TAG_NAME, "div")
            except Exception as e:
                print("exception")
                continue
            list_data = inner_div.text.split("\n")
            if len(list_data)<10:
                continue
            if list_data[0].isnumeric():
                del list_data[0]
            if list_data[1].isnumeric():
                del list_data[1]
            if len(list_data)<10:
                continue
            # if the first number after the 2 teams is the score...
            if list_data[2][0] not in {"+", "-"}:
                team1moneyline = list_data[5].replace(u'\u2212', '-')
                team2moneyline = list_data[10].replace(u'\u2212', '-')
            else:
                team1moneyline = list_data[4].replace(u'\u2212', '-')
                team2moneyline = list_data[9].replace(u'\u2212', '-')
            print(list_data)
            team1 = list_data[0]
            team2 = list_data[1]
            print("FANDUEL: ", set(team1 + team2), team1 + team2)
            # test to make sure each moneyline is valid -> i.e. the table is filled
            try:
                eval(team1moneyline)
                eval(team2moneyline)
            except Exception as e:
                continue
            ascii_bytes = ''.join(set(team1 + team2)).encode('ascii')
            base64_bytes = base64.b64encode(ascii_bytes)
            new_id = base64_bytes.decode('ascii')
            new_id = "FANDUEL-CBB-" + new_id
            newentry = {team1:team1moneyline, team2:team2moneyline}
            self.data[new_id] = newentry
