#import urllib2
from urllib.request import urlopen
from bs4 import BeautifulSoup

#scraping URL
pages = 'https://carros.tucarro.com.co/'

page = urlopen(pages)

soup = BeautifulSoup(page,'html.parser')

#print(soup.prettify())
car_name_box = soup.find('span', attrs={'class':'main-title'})
print(car_name_box)
#car_name = car_name_box.text.strip()

#print(car_name)
