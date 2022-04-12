from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Open 2048 website game
browser = webdriver.Chrome("chromedriver.exe")
browser.get('https://gabrielecirulli.github.io/2048/')

html_elem = browser.find_element_by_tag_name('html')

while True:
    html_elem.send_keys(Keys.UP)
    html_elem.send_keys(Keys.RIGHT)
    html_elem.send_keys(Keys.DOWN)
    html_elem.send_keys(Keys.LEFT)


