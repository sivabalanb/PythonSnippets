import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
})

def find_iata(url):
	Link = requests.get(url_iata_europe, headers=headers)
	soup =BeautifulSoup(Link.content,"lxml")
	airport_names =  soup.find_all('tr')
	code_of_airport = []
	for airport_name in airport_names:
		try:
			individual_airport = airport_name.find_all('td')
			name_of_airport = individual_airport[3].text
			iata = individual_airport[1].text
			if len(individual_airport[1].text) == 3:
				code_of_airport.append(individual_airport[1].text)

		except Exception as e:
			print("Error while extracting the code:\t", e)
			pass
	return code_of_airport

url_iata_asia = "https://airportcodes.io/en/continent/asia/"
url_iata_europe = "https://airportcodes.io/en/continent/europe/"

asia = find_iata(url_iata_asia)
europe = find_iata(url_iata_europe)

print("Asia:\t", asia)
print("Europe:\t", europe)