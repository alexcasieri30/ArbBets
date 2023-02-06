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


class DraftKingsCBB(ArbTemplate):
    def __init__(self, executable_path, headless=True):
        self.data = {}
        if headless:
            self.driver = webdriver.Chrome(executable_path, chrome_options=options)
        else:
            self.driver = webdriver.Chrome(executable_path)
        self.url = "https://sportsbook.draftkings.com/leagues/basketball/ncaab"
        self.sport = "CBB"
        self.book = "DraftKings"

    def get_data_snapshot(self):
        tbody = self.driver.find_element(By.XPATH, '//*[@id="root"]/section/section[2]/section/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/table/tbody')
        rows = tbody.find_elements(By.XPATH, "tr")
        event = {}
        event_name = ""
        for i, row in enumerate(rows):
            rowdata = row.find_elements(By.TAG_NAME, "td")
            team = row.find_element(By.TAG_NAME, 'th').find_element(By.TAG_NAME, 'a').find_element(By.CLASS_NAME, 'event-cell').text
            teamdata = None
            for k, col in enumerate(rowdata):
                teamdata = col.text.split("\n")[-1]
            team = remove_pattern(team)
            event[team] = teamdata.replace(u'\u2212', '-')
            event_name += team
            if i%2==1:
                print("DRAFTKINGS: ", set(event_name), event_name)
                ascii_bytes = ''.join(set(event_name)).encode('ascii')
                base64_bytes = base64.b64encode(ascii_bytes)
                new_id = base64_bytes.decode('ascii')
                new_id = "DRAFTKINGS-CBB-" + new_id
                self.data[new_id] = event
                event = {}
                event_name = ""

import re

def remove_pattern(string):
    return re.sub(r"\n\d+\Z", "", string)