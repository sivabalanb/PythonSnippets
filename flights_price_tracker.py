import requests
from bs4 import BeautifulSoup
import os
import time
import csv


def find_the_prices(url):
	
	headers = requests.utils.default_headers()
	headers.update({
	    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
	})

	Link = requests.get(url, headers=headers)
	soup =BeautifulSoup(Link.content,"lxml")

	#hotel_name =  soup.find('title')
	#hotel_name = hotel_name.text

	tags = soup.findAll("span", {"class": "amount-text"})
	price = []
	for tag in tags:
		price_t = tag.text
		print(price_t.text)
		

url='https://www.airasia.com/booking/select/en/gb/MAA/HKT/2019-03-08/N/1/0/0/O/N/INR/SC'

find_the_prices(url)
#<jsl jstcache="9495">₹&nbsp;6,081</jsl>