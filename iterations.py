#import urllib2
from urllib.request import urlopen
from bs4 import BeautifulSoup
from time import sleep
import csv
from selenium import webdriver


data = []
pages = 'https://carros.tucarro.com.co/'
page = urlopen(pages)
soup = BeautifulSoup(page,'html.parser')
#firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.get(pages)

python_function = driver.find_element_by_class_name('images-viewer')
#print(python_function)
python_function.click()
soup_results_section = BeautifulSoup(driver.page_source, 'html.parser')
#price = soup_results_section.body.main.div.
item_url = driver.current_url;
print(item_url)

price_box = soup_results_section.find('span', attrs={'class':'price-tag-fraction'})
price = price_box.text.strip()
print(price)

specs_box = soup_results_section.find_all('li', attrs={'class':'specs-item'})
for thing in specs_box:
    print(thing.text.strip())

location_box = soup_results_section.find('div', attrs={'class':'location-info'})
location = location_box.text.strip()
print(location_box)

# with open('car-prices.txt', 'w') as text_file:
#     text_file.write(str(soup))
# sleep(1)
# ol = soup.body.main.div.div.div.section.next_sibling
# print(ol)
#all_ol = soup.find_all('ol')
# parsed_all_ol = BeautifulSoup(all_ol,'html.parser')
# print(parsed_all_ol)
#print(len(all_ol.children))
#a = 0
#print(soup.prettify())
#for items in soup:
    #scraping URL
#    pages = 'https://carros.tucarro.com.co/'
#    page = urlopen(pages)
#    soup = BeautifulSoup(page,'html.parser')
    #print(soup.prettify())
#    car_name_box = soup.find('span', attrs={'class':'main-title'})
    #print(car_name_box)
#    car_name = car_name_box.text.strip()

#    print(car_name)

    ##car_price_box = soup.find('span', attrs={'class':'price__fraction'})
    ##car_price = car_price_box.text.strip()

    ##print(car_price)

#    items = soup.find('div', attrs={'class':"nav-main-content"})
#    print(items)
#    print(a)
#    a = a + 1
#    sleep(2)
