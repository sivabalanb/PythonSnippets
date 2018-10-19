import wget
import requests
from bs4 import BeautifulSoup
url = "https://www.yoururl.com/"
Link = requests.get(url)
soup =BeautifulSoup(Link.content,"lxml")
scripts = soup.find_all("td")

for script in scripts:
    if script.text == "text_that_you_are_searching":
    	filename = str(script.text) +".csv"
        download = "https://www.yoururl.com/"+str(script.a['href'])+"?response_type=csv"
        response = requests.get(download, stream=True)
    
	with open(filename, 'wb') as handle:
			for block in response.iter_content(1024):
				handle.write(block)