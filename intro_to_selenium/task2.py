import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#infra - העמדה
driver = webdriver.Chrome()

#infra        #logic
driver.get('https://www.google.com')

#logic
search_input = driver.find_element(By.XPATH, '//input[@id="Search"]')
search_input.send_keys('Python programming')
search_input.send_keys(Keys.RETURN)
time.sleep(2)
print(driver.title)


#infra
driver.quit()