import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
 
#-- Setup
options = Options()
options.add_argument("--headless")
browser = webdriver.Firefox(firefox_options=options, executable_path=r"C:\Users\thanman\Downloads\geckodriver-v0.24.0-win64\geckodriver.exe")
#-- Parse
browser.get('https://shop.coles.com.au/a/a-national/product/coles-tuna-cat-food')
soup = BeautifulSoup(browser.page_source, 'div')
welcome = soup.select('head > title')
print(welcome.text)