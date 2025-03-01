from selenium import webdriver
import time

#biblioteka napisana obiektowo

okno1_chrome = webdriver.Chrome()
okno1_chrome.get('https://www.google.com/')

#nie mam firefoxa więc nie sprawdze
# okno2_firefox = webdriver.Firefox()
# okno2_chrome.get('https://www.allegro.com/')
#okno2_firefox.close()

#tu też sleep(3) można robić

