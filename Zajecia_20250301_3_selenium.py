from selenium import webdriver
from selenium.webdriver import Keys
from time import sleep

#biblioteka napisana obiektowo

okno1_chrome = webdriver.Chrome()
okno1_chrome.get('https://www.google.com/')

#nie mam firefoxa więc nie sprawdze
# okno2_firefox = webdriver.Firefox()
# okno2_chrome.get('https://www.allegro.com/')
#okno2_firefox.close()

#tu też sleep(3) można robić

okno1_chrome.find_element('id','L2AGLb').click()
sleep(3)

search_field = okno1_chrome.find_element('name','q')
search_field.send_keys('Czy chat GPT opanuje świat?')
sleep(5)
search_field.send_keys(Keys.ENTER)
sleep(3)

okno1_chrome.close()
#okno2_firefox.close()