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


# for this one Selenium needs to make a click on the cbb tab
# //*[@id="highlights__prematch__sport__basketball"]

class FoxBetCBB(ArbTemplate):
    def __init__(self, executable_path, headless=True):
        self.data = {}
        if headless:
            self.driver = webdriver.Chrome(executable_path, chrome_options=options)
        else:
            self.driver = webdriver.Chrome(executable_path)
        self.url = "https://nj.foxbet.com/"
        self.sport = "CBB"
        self.book = "FoxBet"


    def get_data_snapshot(self):
        self.driver.maximize_window() # For maximizing window
        self.driver.implicitly_wait(30)
        element = self.driver.find_element(By.ID,'highlights__prematch__sport__basketball')
        self.driver.execute_script("arguments[0].click();", element)
        market_content = self.driver.find_element(By.CLASS_NAME, 'market-content')
        games = market_content.find_elements(By.TAG_NAME, "section")
        for game in games:
            game_info = game.find_elements(By.TAG_NAME, "div")[0]
            # print(game_info.text)
            game_info_list = game_info.text.split("\n")
            print(game_info_list)
            team1 = remove_pattern(game_info_list[0])
            team2 = remove_pattern(game_info_list[1])
            if game_info_list[2][0] in {"+", "-"}:
                team1moneyline = game_info_list[9].replace(u'\u2212', '-')
                team2moneyline = game_info_list[4].replace(u'\u2212', '-')
            else:
                team1moneyline = game_info_list[11].replace(u'\u2212', '-')
                team2moneyline = game_info_list[6].replace(u'\u2212', '-')
            try:
                if abs(eval(team1moneyline))<100 or abs(eval(team2moneyline))<100:
                    continue
            except Exception as e:
                print("OTB: continuing")
                continue
            event_name = team1 + team2
            print("FOXBET: ", set(event_name), event_name)
            ascii_bytes = ''.join(set(event_name)).encode('ascii')
            base64_bytes = base64.b64encode(ascii_bytes)
            new_id = base64_bytes.decode('ascii')
            new_id = "FOXBET-CBB-" + new_id
            event = {team1: team1moneyline.replace(u'\u2212', '-'), team2: team2moneyline.replace(u'\u2212', '-')}
            self.data[new_id] = event
            # .find_elements(By.TAG_NAME, "div")[0]
            # print(div_div.text)

import re
def remove_pattern(string):
    return re.sub(r'^#\d{1,2}\s', '', string)
