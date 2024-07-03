from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#infra
driver = webdriver.Chrome()

#infra       #logic
driver.get("https://www.youtube.com//")

#logic
search_input = driver.find_element(By.XPATH, '//input[@id="Search"]')
search_input.send_keys("barcelona")
search_input.send_keys(Keys.RETURN)


#infra
driver.quit()