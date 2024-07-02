from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://ultimateqa.com/simple-html-elements-for-automation/')
Simple_Controls = driver.find_element(By.XPATH, '//a[text()="Click Me"]')
Simple_Controls.click()
Simple_Controls = driver.find_element(By.XPATH, '//*[@id="post-4690"]/div[1]/h1')
print(Simple_Controls.text)

driver.quit()


