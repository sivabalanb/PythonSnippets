urls = ["https://www.google.com/travel/hotels/Pa%20Tong/place/15124167736024278125?ap=MAFaUgoFCPAuEAAiA0lOUioWCgcI4w8QARgPEgcI4w8QARgQGAEoADgEOAVyAggCmgEIEgZQYXRvbmeiARMKCS9tLzA0NHRkNRIGUGF0b25nkgECIAFwAA&g2lb=4181926%2C4208993%2C4209588%2C4223281%2C4225904%2C4227717%2C4207631%2C4215556%2C4220469%2C4226109&hl=en&gl=in&un=0&q=4%20star%20hotels%20patong&rp=OAFAAA&ictx=1&ved=0CKYBEKjgAigLahcKEwig5Oumn7DfAhUAAAAAHQAAAAAQEA&hrf=CgUI8C4QACIDSU5SKhYKBwjjDxADGAkSBwjjDxADGAwYAyABOAQ4BXICCAKaAQgSBlBhdG9uZ6IBEwoJL20vMDQ0dGQ1EgZQYXRvbmeSAQIgAQ&tcfs=Ei0KCS9tLzA0NHRkNRIGUGF0b25nGhgKCjIwMTktMDMtMDkSCjIwMTktMDMtMTIYAiIYCgoyMDE5LTAzLTA5EgoyMDE5LTAzLTEyUgJIBA",
"https://www.google.com/travel/hotels/Pa%20Tong/place/7507267568307879052?ap=MAFaUAoFCPAuEAAiA0lOUioWCgcI4w8QAxgJEgcI4w8QAxgMGAMgATgFcgIIAZoBCBIGUGF0b25nogETCgkvbS8wNDR0ZDUSBlBhdG9uZ5IBAiABcAA&g2lb=4181926%2C4208993%2C4209588%2C4223281%2C4225904%2C4227717%2C4207631%2C4215556%2C4220469%2C4226109&hl=en&gl=in&un=0&q=4%20star%20hotels%20patong&rp=OAFAAA&ictx=1&ved=0CCgQqOACKAJqFwoTCKDk66afsN8CFQAAAAAdAAAAABBS&hrf=CgUI8C4QACIDSU5SKhYKBwjjDxADGAkSBwjjDxADGAwYAyABOAVoA3ICCAGaAQgSBlBhdG9uZ6IBEwoJL20vMDQ0dGQ1EgZQYXRvbmeSAQIgAQ&tcfs=Ei0KCS9tLzA0NHRkNRIGUGF0b25nGhgKCjIwMTktMDMtMDkSCjIwMTktMDMtMTIYASIYCgoyMDE5LTAzLTA5EgoyMDE5LTAzLTEyUgJIBQ",
"https://www.google.com/travel/hotels/Pa%20Tong/place/12760924574243379521?ap=MAFaUAoFCPAuEAAiA0lOUioWCgcI4w8QAxgJEgcI4w8QAxgMGAMgATgFcgIIAZoBCBIGUGF0b25nogETCgkvbS8wNDR0ZDUSBlBhdG9uZ5IBAiABcAA&g2lb=4181926%2C4208993%2C4209588%2C4223281%2C4225904%2C4227717%2C4207631%2C4215556%2C4220469%2C4226109&hl=en&gl=in&un=0&q=4%20star%20hotels%20patong&rp=OAFAAA&ictx=1&ved=0CJgBEKjgAigKahcKEwig5Oumn7DfAhUAAAAAHQAAAAAQUg&hrf=CgUI8C4QACIDSU5SKhYKBwjjDxADGAkSBwjjDxADGAwYAyABOAVoA3ICCAGaAQgSBlBhdG9uZ6IBEwoJL20vMDQ0dGQ1EgZQYXRvbmeSAQIgAQ&tcfs=Ei0KCS9tLzA0NHRkNRIGUGF0b25nGhgKCjIwMTktMDMtMDkSCjIwMTktMDMtMTIYASIYCgoyMDE5LTAzLTA5EgoyMDE5LTAzLTEyUgJIBQ"]

import requests
from bs4 import BeautifulSoup

for url in urls:
	headers = requests.utils.default_headers()
	headers.update({
	    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
	})

	Link = requests.get(url, headers=headers)
	soup =BeautifulSoup(Link.content,"lxml")

	hotel_name =  soup.find('title')
	hotel_name = hotel_name.text
	tags = soup.findAll("span", {"class": "eDCB7b"})
	price = []
	for tag in tags:
	    price_t = tag.text.encode("utf-8")[5:]
	    price_t = int(price_t.replace(",", ""))
	    price.append(price_t)

	#print(price)
	#print("Minimum price:\t",min(price))
	#print("Maximum price:\t",max(price))
	my_hotel_dict = {}

	my_hotel_dict[hotel_name] = [min(price),max(price)]

	print(my_hotel_dict)