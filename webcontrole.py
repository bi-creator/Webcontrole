import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
chrome_options = Options()
chrome_options.add_experimental_option('detach',True)
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument("start-maximized")
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://mws.mongodb.com/")
driver.find_element(by=By.CLASS_NAME,value='mws-shell').click()
time.sleep(10)
print('trying to click')
# driver.find_element(by=By.CLASS_NAME,value='CodeMirror-line').click()
time.sleep(10)
elements=driver.find_element(by=By.XPATH,value='/html/body/div/div[1]/div[2]/div[6]/div[1]/div/div/div/div[5]/pre/span/span')
# driver.execute_script("arguments[0].innerText = 'aaaaaaaa'", elements)

