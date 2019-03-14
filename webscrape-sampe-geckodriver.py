from selenium import webdriver
from os import getcwd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Firefox
from fake_useragent import UserAgent

useragent = UserAgent()

profile  = webdriver.FirefoxProfile()
#profile .set_preference("browser.privatebrowsing.autostart", True)
profile .set_preference("general.useragent.override", useragent.random)

driver = webdriver.Firefox(firefox_profile=profile , executable_path=r"C:\Users\thanman\Downloads\geckodriver-v0.24.0-win64\geckodriver.exe")

driver.get('https://shop.coles.com.au/a/a-national/product/coles-tuna-cat-food')
#driver.get( 'https://www.gossiplankanews.com/')

# Print the first 300 characters on the page.
#print(driver.page_source)

driver.quit()
