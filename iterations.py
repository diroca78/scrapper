from urllib.request import urlopen
from bs4 import BeautifulSoup
from time import sleep
import csv
import pandas
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

pages = 'https://carros.tucarro.com.co/'
page = urlopen(pages)
soup = BeautifulSoup(page,'html.parser')

#firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.get(pages)
actions = ActionChains(driver)

#get images array
images_matrix = driver.find_elements_by_xpath ("//div[@class='images-viewer']")
urls_list = []

# #Get URL from each item on page
# with open("source.txt","w") as new_file:
#     for source in images_matrix:
#         urls_list.append(source.get_attribute("item-url"))
#         with open("source.txt","a") as source_file:
#             source_file.write(source.get_attribute("item-url") + "\n")
#
# #print(urls_list)
# #iterate over URLs to get Detailed info
# data = {} #final dictionary per page
# data_columns = ['ITEM','MARCA','MODELO','PRECIO','AÑO','KILOMETRAJE','COMBUSTIBLE','VERSION','COLOR','DIRECCION','TRANSMISSION','TRACCION']
# index = 0
# for url in urls_list:
#     new_page = urlopen(url)
#     new_soup = BeautifulSoup(new_page,'html.parser')
#     specs = {}
#
#     ## Get the price
#     price_box = new_soup.find('span', attrs={'class':'price-tag-fraction'})
#     price = price_box.text.strip() #Format
#     specs['Precio'] = price
#
#     ## Get specificacions
#     specs_box = new_soup.find_all('li', attrs={'class':'specs-item'})
#     for thing in specs_box:
#         thing_to_string = thing.text.strip()
#         string_to_list = thing_to_string.replace('\n',',')
#         string_to_list = string_to_list.split(',')
#         for string in string_to_list:
#             specs[string_to_list[0]] = string_to_list[1]
#
#     ## Get location
#     location_box = new_soup.find('div', attrs={'class':'location-info'})
#     location = location_box.text.strip().strip('El vehículo está en ')
#     specs['Ubicacion'] = location
#     data[index] = specs
#     index = index + 1

next_page_element = driver.find_element_by_xpath("//li[@class='andes-pagination__button andes-pagination__button--next ']")
pagenum = 1
try:
    while next_page_element != '':


        #get images array
        images_matrix = driver.find_elements_by_xpath ("//div[@class='images-viewer']")
        urls_list = []

        #Get URL from each item on page
        with open("source.txt","w") as new_file:
            for source in images_matrix:
                urls_list.append(source.get_attribute("item-url"))
                with open("source.txt","a") as source_file:
                    source_file.write(source.get_attribute("item-url") + "\n")

        #print(urls_list)
        #iterate over URLs to get Detailed info
        data = {} #final dictionary per page
        data_columns = ['ITEM','MARCA','MODELO','PRECIO','AÑO','KILOMETRAJE','COMBUSTIBLE','VERSION','COLOR','DIRECCION','TRANSMISSION','TRACCION']
        index = 0
        for url in urls_list:
            new_page = urlopen(url)
            new_soup = BeautifulSoup(new_page,'html.parser')
            specs = {}
            specs['URL'] = url

            ## Get the price
            price_box = new_soup.find('span', attrs={'class':'price-tag-fraction'})
            price = price_box.text.strip() #Format
            specs['Precio'] = price

            ## Get specificacions
            specs_box = new_soup.find_all('li', attrs={'class':'specs-item'})
            for thing in specs_box:
                thing_to_string = thing.text.strip()
                string_to_list = thing_to_string.replace('\n',',')
                string_to_list = string_to_list.split(',')
                for string in string_to_list:
                    specs[string_to_list[0]] = string_to_list[1]

            ## Get location
            location_box = new_soup.find('div', attrs={'class':'location-info'})
            location = location_box.text.strip().strip('El vehículo está en ')
            specs['Ubicacion'] = location
            data[index] = specs
            index = index + 1

            print(data)
            exit()



        print(f'page number is: {pagenum}')
        print('\n\n\n')
        pagenum+=1
        next_page_element = ''
        next_page_element = driver.find_element_by_xpath("//li[@class='andes-pagination__button andes-pagination__button--next ']")
        driver.find_element_by_xpath("//li[@class='andes-pagination__button andes-pagination__button--next ']").click()
except (NoSuchElementException):
    print("NoElement, Scraping ended, last page!")
    driver.close()
    exit()


#print(f"clicked: {next_page_element}")
sleep(10)
# print(data)
# print('\n')
# print(type(data))
driver.close()
exit()
