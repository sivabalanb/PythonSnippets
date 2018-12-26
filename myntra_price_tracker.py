import requests
from bs4 import BeautifulSoup
import os
import time
import csv
import json

def find_the_prices(url, price_dict):
	
	headers = requests.utils.default_headers()
	headers.update({
	    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
	})

	Link = requests.get(url, headers=headers)
	soup =BeautifulSoup(Link.content,"lxml")

	price_json = soup.find_all("script",type="application/ld+json")
	
	for js in price_json:
		js_t = json.loads(js.text)
		try:
			price_dict[js_t["description"]] = js_t["offers"]['price']
		except Exception as e:
			print("Unable to find the key in json:\t",e)

	print(price_dict)
	return price_dict
	
def write_to_csv(my_price_dict, filename):

	file_exists = os.path.isfile(filename)
	try:
		with open(filename, 'a') as f:  # Just use 'w' mode in 3.x
		    w = csv.DictWriter(f, my_price_dict.keys())
		    if not file_exists:
		    	w.writeheader()
		    w.writerow(my_price_dict)

	except Exception as e:
		print("Error in write_to_csv:\t",e)

if __name__ == '__main__':

	#Bowerbird black jeans, puma BMW wallet, FCUK Blue shirt

	urls = ['https://www.myntra.com/2103997', 'https://www.myntra.com/6699066', 'https://www.myntra.com/2094721']

	my_price_dict = {}

	for url in urls:
		my_price_dict = find_the_prices(url, my_price_dict)
		time.sleep(20)
	write_to_csv(my_price_dict, 'myntra_price_tracker.csv')




