# -*- coding: utf-8 -*-

import os
import time
import csv

import time
from selenium import webdriver

import sendgrid

#Sending mail using sendgrid
def sendgrid_mail(url, price):
	sg = sendgrid.SendGridClient('removedthekey')
	message = sendgrid.Mail()
	message.add_to("youremail@gmail.com")
	message.set_from("youremail2@gmail.com")
	subject = "Flight price is now\t" + str(price)
	print("Subject in sendgrid_mail:\t",subject)
	message.set_subject(subject)
	message.set_html(url)
	sg.send(message)

def find_prices(url):
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument('--disable-dev-shm-usage')
	driver = webdriver.Chrome('/usr/bin/chromedriver',chrome_options=chrome_options)
	#driver = webdriver.Chrome('C:\\Users\\SSubra02\\Documents\\testCode\\chromedriver',chrome_options=chrome_options)	
	driver.get(url);
	time.sleep(10) # Let the user actually see something!

	prices = driver.find_elements_by_class_name("actual-price")
	price_list = []
	
	for price in prices:
		price_t = price.text
		price_t = price_t[3:].replace(",", "")
		if int(price_t) < 6000:
			sendgrid_mail(url, price_t)
			print("Its a deal!")
		price_list.append(price_t)

	driver.quit()

	return price_list

def write_to_csv(my_flight_prices, filename):
	#os.chdir('/home/user/csv_files')
	file_exists = os.path.isfile(filename)
	try:
		with open(filename, 'a') as f:
			writer = csv.writer(f)
			writer.writerow(my_flight_prices)

	except Exception as e:
		print("Error in write_to_csv:\t",e)

if __name__ == '__main__':
	
	url='https://www.makemytrip.com/air/search?tripType=O&itinerary=MAA-HKT-D-08Mar2019&paxType=A-1&cabinClass=E'

	prices = find_prices(url)
	print("List of prices:\t", prices)
	write_to_csv(prices,'flight_price.csv')
