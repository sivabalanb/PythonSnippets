import requests
from bs4 import BeautifulSoup
import os
import time
import csv

# Read the CSV to compare it to old prices
def read_csv():
	try:
		with open('price_tracker.csv') as csv_file:
			reader = csv.reader(csv_file)
			old_prices = DictReader(reader)
			print(old_prices)

	except Exception as e:
		old_prices = {}
		print("Failed to read the csv:\t",e)

	return old_prices

# Looping through the given list of hotel to find the prices
def find_the_prices(url):
	
	headers = requests.utils.default_headers()
	headers.update({
	    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
	})

	Link = requests.get(url, headers=headers)
	soup =BeautifulSoup(Link.content,"lxml")

	hotel_name =  soup.find('title')
	hotel_name = hotel_name.text

	tags = soup.findAll("span", {"class": "eDCB7b"})
	price = []
	for tag in tags:
		price_t = tag.text.encode("utf-8")[5:]
		price_decoded = str(price_t, 'utf-8')
		
		price_t = price_decoded.replace(",", "")
		try:
			price_t = int(price_t)
		except Exception as e:
			print("Exception while converting the price to integer:\t",price_t)
		
		if isinstance(price_t, int):
			price.append(price_t)

	print(price)
	print("{} -->\tMinimum price: {} \tMaximum price: {}".format(hotel_name,min(price),max(price)))
	
	my_hotel_dict[hotel_name] = min(price)
	print(my_hotel_dict)

	return my_hotel_dict

def write_to_csv(my_hotel_dict):

	filename = 'price_tracker.csv'
	#old_prices = read_csv()
	file_exists = os.path.isfile(filename)
	try:
		with open(filename, 'a') as f:  # Just use 'w' mode in 3.x
		    w = csv.DictWriter(f, my_hotel_dict.keys())
		    if not file_exists:
		    	w.writeheader()
		    w.writerow(my_hotel_dict)

	except Exception as e:
		print("Error in write_to_csv:\t",e)

if __name__ == '__main__':

	urls = [#"https://www.google.com/travel/hotels/Pa%20Tong/place/15124167736024278125?ap=MAFaUgoFCPAuEAAiA0lOUioWCgcI4w8QARgPEgcI4w8QARgQGAEoADgEOAVyAggCmgEIEgZQYXRvbmeiARMKCS9tLzA0NHRkNRIGUGF0b25nkgECIAFwAA&g2lb=4181926%2C4208993%2C4209588%2C4223281%2C4225904%2C4227717%2C4207631%2C4215556%2C4220469%2C4226109&hl=en&gl=in&un=0&q=4%20star%20hotels%20patong&rp=OAFAAA&ictx=1&ved=0CKYBEKjgAigLahcKEwig5Oumn7DfAhUAAAAAHQAAAAAQEA&hrf=CgUI8C4QACIDSU5SKhYKBwjjDxADGAkSBwjjDxADGAwYAyABOAQ4BXICCAKaAQgSBlBhdG9uZ6IBEwoJL20vMDQ0dGQ1EgZQYXRvbmeSAQIgAQ&tcfs=Ei0KCS9tLzA0NHRkNRIGUGF0b25nGhgKCjIwMTktMDMtMDkSCjIwMTktMDMtMTIYAiIYCgoyMDE5LTAzLTA5EgoyMDE5LTAzLTEyUgJIBA",
			"https://www.google.com/travel/hotels/Pa%20Tong/place/7507267568307879052?ap=MAFaUAoFCPAuEAAiA0lOUioWCgcI4w8QAxgJEgcI4w8QAxgMGAMgATgFcgIIAZoBCBIGUGF0b25nogETCgkvbS8wNDR0ZDUSBlBhdG9uZ5IBAiABcAA&g2lb=4181926%2C4208993%2C4209588%2C4223281%2C4225904%2C4227717%2C4207631%2C4215556%2C4220469%2C4226109&hl=en&gl=in&un=0&q=4%20star%20hotels%20patong&rp=OAFAAA&ictx=1&ved=0CCgQqOACKAJqFwoTCKDk66afsN8CFQAAAAAdAAAAABBS&hrf=CgUI8C4QACIDSU5SKhYKBwjjDxADGAkSBwjjDxADGAwYAyABOAVoA3ICCAGaAQgSBlBhdG9uZ6IBEwoJL20vMDQ0dGQ1EgZQYXRvbmeSAQIgAQ&tcfs=Ei0KCS9tLzA0NHRkNRIGUGF0b25nGhgKCjIwMTktMDMtMDkSCjIwMTktMDMtMTIYASIYCgoyMDE5LTAzLTA5EgoyMDE5LTAzLTEyUgJIBQ",
			"https://www.google.com/travel/hotels/Pa%20Tong/place/12760924574243379521?ap=MAFaUAoFCPAuEAAiA0lOUioWCgcI4w8QAxgJEgcI4w8QAxgMGAMgATgFcgIIAZoBCBIGUGF0b25nogETCgkvbS8wNDR0ZDUSBlBhdG9uZ5IBAiABcAA&g2lb=4181926%2C4208993%2C4209588%2C4223281%2C4225904%2C4227717%2C4207631%2C4215556%2C4220469%2C4226109&hl=en&gl=in&un=0&q=4%20star%20hotels%20patong&rp=OAFAAA&ictx=1&ved=0CJgBEKjgAigKahcKEwig5Oumn7DfAhUAAAAAHQAAAAAQUg&hrf=CgUI8C4QACIDSU5SKhYKBwjjDxADGAkSBwjjDxADGAwYAyABOAVoA3ICCAGaAQgSBlBhdG9uZ6IBEwoJL20vMDQ0dGQ1EgZQYXRvbmeSAQIgAQ&tcfs=Ei0KCS9tLzA0NHRkNRIGUGF0b25nGhgKCjIwMTktMDMtMDkSCjIwMTktMDMtMTIYASIYCgoyMDE5LTAzLTA5EgoyMDE5LTAzLTEyUgJIBQ"]
			#"https://www.google.com/travel/hotels/Pa%20Tong/place/997620782875815276?ap=EgNDQXcwA1pQCgUI8C4QACIDSU5SKhYKBwjjDxADGAkSBwjjDxADGAwYAyABaANyAggBmgEIEgZQYXRvbmeiARMKCS9tLzA0NHRkNRIGUGF0b25nkgECIAFwAA&g2lb=4181926%2C4208993%2C4209588%2C4223281%2C4225904%2C4227717%2C4207631%2C4215556%2C4220469%2C4226109&hl=en&gl=in&un=0&q=4%20star%20hotels%20patong&rp=OAFAAA&ictx=1&ved=0CJgBEKjgAigKahcKEwiA6qKyq7DfAhUAAAAAHQAAAAAQIw&hrf=CgUI8C4QACIDSU5SKhYKBwjjDxADGAkSBwjjDxADGAwYAyABOARoA3ICCAGaAQgSBlBhdG9uZ6IBEwoJL20vMDQ0dGQ1EgZQYXRvbmeSAQIgAQ&tcfs=Ei0KCS9tLzA0NHRkNRIGUGF0b25nGhgKCjIwMTktMDMtMDkSCjIwMTktMDMtMTIYASIYCgoyMDE5LTAzLTA5EgoyMDE5LTAzLTEyUgJIBA",
			#"https://www.google.com/travel/hotels/Pa%20Tong/place/8443959769382945276?ap=EgNDREEwA1pQCgUI8C4QACIDSU5SKhYKBwjjDxADGAkSBwjjDxADGAwYAyABaANyAggBmgEIEgZQYXRvbmeiARMKCS9tLzA0NHRkNRIGUGF0b25nkgECIAFwAA&g2lb=4181926%2C4208993%2C4209588%2C4223281%2C4225904%2C4227717%2C4207631%2C4215556%2C4220469%2C4226109&hl=en&gl=in&un=0&q=4%20star%20hotels%20patong&rp=OAFAAA&ictx=1&ved=0CJgBEKjgAigKahcKEwiA6qKyq7DfAhUAAAAAHQAAAAAQSw&hrf=CgUI8C4QACIDSU5SKhYKBwjjDxADGAkSBwjjDxADGAwYAyABOARoA3ICCAGaAQgSBlBhdG9uZ6IBEwoJL20vMDQ0dGQ1EgZQYXRvbmeSAQIgAQ&tcfs=Ei0KCS9tLzA0NHRkNRIGUGF0b25nGhgKCjIwMTktMDMtMDkSCjIwMTktMDMtMTIYASIYCgoyMDE5LTAzLTA5EgoyMDE5LTAzLTEyUgJIBA",
			#"https://www.google.com/travel/hotels/Pa%20Tong/place/11616903417879953370?ap=EgNDREEwA1pQCgUI8C4QACIDSU5SKhYKBwjjDxADGAkSBwjjDxADGAwYAyABaANyAggBmgEIEgZQYXRvbmeiARMKCS9tLzA0NHRkNRIGUGF0b25nkgECIAFwAA&g2lb=4181926%2C4208993%2C4209588%2C4223281%2C4225904%2C4227717%2C4207631%2C4215556%2C4220469%2C4226109&hl=en&gl=in&un=0&q=4%20star%20hotels%20patong&rp=OAFAAA&ictx=1&ved=0CIoBEKjgAigJahcKEwiA6qKyq7DfAhUAAAAAHQAAAAAQSw&hrf=CgUI8C4QACIDSU5SKhYKBwjjDxADGAkSBwjjDxADGAwYAyABOARoA3ICCAGaAQgSBlBhdG9uZ6IBEwoJL20vMDQ0dGQ1EgZQYXRvbmeSAQIgAQ&tcfs=Ei0KCS9tLzA0NHRkNRIGUGF0b25nGhgKCjIwMTktMDMtMDkSCjIwMTktMDMtMTIYASIYCgoyMDE5LTAzLTA5EgoyMDE5LTAzLTEyUgJIBA"]

	my_hotel_dict = {}

	for url in urls:
		my_hotel_dict = find_the_prices(url)
		time.sleep(10)
	print("my_hotel_dict before writing it to csv:\t",my_hotel_dict)
	write_to_csv(my_hotel_dict)