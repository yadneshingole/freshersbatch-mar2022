import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Activating the chrome browser
driver=webdriver.Chrome("chromedriver.exe")

# Opening the google images
url = "https://images.google.com/"
driver.get(url)

search_bar = driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')    # Finding the search bar using it's xpath
search_bar.send_keys("fruits")       # Inputing "fruits" keyword to search images
search_button = driver.find_element_by_xpath('//*[@id="sbtc"]/button')    # Finding the xpath of search button
search_button.click()        # Clicking the search button

time.sleep(3)

# 500 time we scroll down by 10000 in order to generate more images on the website
for _ in range(500):
    driver.execute_script("window.scrollBy(0,10000)")

images = driver.find_elements_by_xpath('//img[@class="rg_i Q4LuWd"]')

img_urls = []

img_data = []

for image in images:

    source= image.get_attribute('src')

    if source is not None:

        if(source[0:4] == 'http'):
time.sleep(3)

import requests
for i in range(len(img_urls)):

    if i >= 100:

        break

    print("Downloading {0} of {1} images" .format(i, 100))

    response= requests.get(img_urls[i])

    file = open(r"D:\Fliprobo_images\Image\fruits"+str(i)+".jpg", "wb")

    file.write(response.content)

            img_urls.append(source)
