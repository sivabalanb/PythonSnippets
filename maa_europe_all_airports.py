import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import unicodedata

def google_flights(url):
	
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument('--disable-dev-shm-usage')
	
	#driver = webdriver.Chrome('/usr/bin/chromedriver',chrome_options=chrome_options)
	#driver = webdriver.Chrome(r'C:\\Users\\sivabalan.balasu\\Documents\\GitHub\\chromedriver.exe')
	#driver = webdriver.Chrome("C:/Users/sivabalan.balasu/Documents/chromedriver.exe")

	#driver.get(url);
	#prices = driver.find_elements_by_class_name("gws-flights-results__collapsed-itinerary gws-flights-results__itinerary")
	#print("prices:\t",prices.text)
	#item = driver.execute_script("return document.querySelector('.flt-subhead1.gws-flights-results__price.gws-flights-results__cheapest-price span + jsl')")
	#print(item.text)
	#d.quit()

	d = webdriver.Chrome(r'C:\\Users\\sivabalan.balasu\\Documents\\GitHub\\chromedriver.exe', chrome_options=chrome_options)
	#gws-flights-results__collapsed-itinerary gws-flights-results__itinerary
	#url='https://www.google.es/flights?lite=0#flt=/m/0h3tv./m/05qtj.2018-12-14;c:EUR;e:1;a:FR;sd:1;t:f;tt:o'
	d.get(url)
	time.sleep(5)
	page = BeautifulSoup(d.page_source, 'html.parser')
	#print("page:\t", page)
	#precios = page.findAll(gws-flights-results__collapsed-itinerary)
	tags = page.findAll("div", {"class": "gws-flights-results__collapsed-itinerary"})
	#flt-subhead1 gws-flights-results__price gws-flights-results__cheapest-price
	price = tags[0].find("div",{"class":"gws-flights-results__cheapest-price"})
	print("Price:\t", price.text)
	lowest_price = unicodedata.normalize("NFKD", price.text)
	d.quit();
	print("#"*100)
	return  lowest_price.strip()

def find_airport_codes(final_result):
	headers = requests.utils.default_headers()
	headers.update({
	    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
	})
	url_iata = "https://airmundo.com/en/blog/airport-codes-european-airports/"
	Link = requests.get(url_iata, headers=headers)
	soup =BeautifulSoup(Link.content,"lxml")
	airport_names =  soup.find_all('tr')
	#hotel_name = hotel_name.text
	#individual_airport = airport_name[1].find_all('td')
	#print("Name of airport:\t", individual_airport[1].text)
	#print("Code of airport:\t", individual_airport[2].text)
	code_of_airport = []
	for airport_name in airport_names:
		try:
			individual_airport = airport_name.find_all('td')
			name_of_airport = individual_airport[1].text
			iata = individual_airport[2].text
			name_of_airport = "TIA"
			iata = "Tirana"
			if len(individual_airport[2].text) == 3:
				code_of_airport.append(individual_airport[2].text)
			else:
				print("Not a valid airport code")
		except Exception as e:
			print("Error while extracting the code:\t", e)
			pass

		try:
			url_google_flights = "https://www.google.com/flights?hl=en#flt=/m/0c8tk."+individual_airport[2].text+".2020-03-05;c:INR;e:1;sd:1;t:f;tt:o"
			print("URL accessed using google flights:\t", url_google_flights)
			price = google_flights(url_google_flights)
			time.sleep(30)
			final_result[iata] = [name_of_airport, price]
			print("Updated Final result:\t", final_result)
		except Exception as e:
			print("Error while searching google flights:\t", e)
		
	print("Code of airports:\t", code_of_airport)


final_result = {}
find_airport_codes(final_result)
print("final_result:\t", final_result)

with open('final_price.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in final_result.items():
       writer.writerow([key, value])