# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os
import time
import csv

import time
from selenium import webdriver


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('/usr/bin/chromedriver',chrome_options=chrome_options)
url='https://flight.yatra.com/air-search-ui/seoint/trigger?type=O&viewName=normal&flexi=0&noOfSegments=1&origin=MAA&originCountry=IN&destination=HKT&destinationCountry=TH&flight_depart_date=08/03/2019&ADT=1&CHD=0&INF=0&preferred=AK&class=Economy'
driver.get(url);
time.sleep(10) # Let the user actually see something!
from time import gmtime, strftime
fname = strftime("%m_%d_%H_%M", gmtime()) + ".png"
driver.save_screenshot(fname)
driver.quit()
