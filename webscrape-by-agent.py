from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from fake_useragent import UserAgent

binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
useragent = UserAgent()
profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", useragent.random)
driver = webdriver.Firefox(firefox_profile=profile, firefox_binary=binary, executable_path="C:\\Users\\thanman\\Downloads\\geckodriver-v0.24.0-win64\\geckodriver.exe")
driver.get("https://shop.coles.com.au/a/a-national/product/coles-tuna-cat-food")
driver.quit()