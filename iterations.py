#import urllib2
from urllib.request import urlopen
from bs4 import BeautifulSoup
from time import sleep
import csv
import pandas
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

pages = 'https://carros.tucarro.com.co/'
page = urlopen(pages)
soup = BeautifulSoup(page,'html.parser')

#firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.get(pages)
actions = ActionChains(driver)

#get images array
#python_function = driver.find_element_by_class_name('images-viewer')
#images_matrix = driver.find_elements_by_xpath('//div[contains(@id, "images-viewwer")]//a[contains(@href, "rooms")]')
#images_matrix = driver.find_elements_by_xpath('//div[contains(@id, "images-viewer")]')
images_matrix = driver.find_elements_by_xpath ("//div[@class='images-viewer']")
#images_matrix = driver.find_elements_by_xpath ("//div[@class='item__info ']//a[contains(@href)]")
urls_list = []

#Get URL from each item on page
with open("source.txt","w") as new_file:
    for source in images_matrix:
        #driver.click("item-url")
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
print('\n')
print(type(data))
driver.close()
exit()
















###################################################################################
    #
    # driver = webdriver.Firefox()
    # driver.implicitly_wait(30)
    # driver.get(url)
    # actions = ActionChains(driver)
    # print(driver)
    # actions.click(url).perform()
    # print(f"URL number {count}")
    # count = count + 1
    # #actions.reset_actions()
    # sleep(2)
    # #driver.close()
    #

#
# print(len(images_matrix))#images_matrix = driver.find_elements_by_xpath ("//div[@class='item-link item__js-link']")
# with open("images.txt","w") as new_file:
#     for image in images_matrix:
#         with open("images.txt","a") as images_file:
#             images_file.write(str(image) + "\n")
#     images_file.close()
#
# original_window_handle = driver.current_window_handle
# print(original_window_handle)
#
# for images in images_matrix:
#     print(images)
#     #python_function.click()
#     actions.move_to_element(images)
#     #actions.click(images)
#     actions.key_down(Keys.SHIFT).click(images).key_up(Keys.SHIFT)
#     actions.perform()
#     actions.reset_actions()
#     #actions.key_down(Keys.SHIFT).click(images_matrix[a]).perform()
#
#     sleep(2)
#     #print(len(driver.window_handles))
#     #driver.switch_to.window(driver.window_handles[-1])
#     #handles = driver.window_handles
#     #current_window_handle = driver.current_window_handle
#     #print(handles)
#     #
#     # soup_results_section = BeautifulSoup(driver.page_source, 'html.parser')
#     # item_url = driver.current_url;
#     # print(item_url)
#     #
#     # price_box = soup_results_section.find('span', attrs={'class':'price-tag-fraction'})
#     # price = price_box.text.strip()
#     # print(price)
#     #
#     # specs_box = soup_results_section.find_all('li', attrs={'class':'specs-item'})
#     # for thing in specs_box:
#     #     print(thing.text.strip())
#     #
#     # location_box = soup_results_section.find('div', attrs={'class':'location-info'})
#     # location = location_box.text.strip()
#     # print(location.strip('El vehículo está en '))
#     #
#     sleep(2)
#     #i = 1
#     #while i <= len(driver.window_handles):
#     #    driver.switch_to.window(driver.window_handles[i])
#     #    if wh != original_window_handle:
#     #        print(wh)
#     #        driver.switch_to.window(wh)
#     #    driver.close()
#     #    i = i + 1
#     #sleep(2)
#     #driver.window_handles = original_window_handle
#     #driver.switch_to.window(original_window_handle)
#     #driver.switch_to.window(driver.window_handles[0])
#     #driver.clear_cache(driver)
#     #sleep(2)
#
# #####################################################################################################################
# # with open('car-prices.txt', 'w') as text_file:
# #     text_file.write(str(soup))
# # sleep(1)
# # ol = soup.body.main.div.div.div.section.next_sibling
# # print(ol)
# #all_ol = soup.find_all('ol')
# # parsed_all_ol = BeautifulSoup(all_ol,'html.parser')
# # print(parsed_all_ol)
# #print(len(all_ol.children))
# #a = 0
# #print(soup.prettify())
# #for items in soup:
#     #scraping URL
# #    pages = 'https://carros.tucarro.com.co/'
# #    page = urlopen(pages)
# #    soup = BeautifulSoup(page,'html.parser')
#     #print(soup.prettify())
# #    car_name_box = soup.find('span', attrs={'class':'main-title'})
#     #print(car_name_box)
# #    car_name = car_name_box.text.strip()
#
# #    print(car_name)
#
#     ##car_price_box = soup.find('span', attrs={'class':'price__fraction'})
#     ##car_price = car_price_box.text.strip()
#
#     ##print(car_price)
#
# #    items = soup.find('div', attrs={'class':"nav-main-content"})
# #    print(items)
# #    print(a)
# #    a = a + 1
# #    sleep(2)
