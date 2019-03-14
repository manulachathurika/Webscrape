from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

options = Options()
ua = UserAgent()
userAgent = ua.random
print(userAgent)
options.add_argument(f'user-agent={userAgent}')
options.add_argument("disable-infobars"); 

driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\Users\thanman\Downloads\chromedriver_win32\chromedriver.exe')
driver.get("https://shop.coles.com.au/a/a-national/product/coles-tuna-cat-food")
#driver.get( 'https://www.gossiplankanews.com/')
#driver.quit()