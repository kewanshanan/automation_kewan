from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#first-test
driver = webdriver.Chrome()

driver.get('https://ultimateqa.com/simple-html-elements-for-automation/')
Simple_Controls = driver.find_element(By.XPATH, '//a[text()="Click Me"]')
Simple_Controls.click()
Simple_Controls = driver.find_element(By.XPATH, '//*[@id="post-4690"]/div[1]/h1')
print(Simple_Controls.text)

driver.quit()

#second-test
driver = webdriver.Chrome()
driver.get('https://ultimateqa.com/simple-html-elements-for-automation/')
Simple_Controls = driver.find_element(By.XPATH, '//*[@id="et_pb_contact_name_0"]')
Simple_Controls.click()
Simple_Controls.send_keys('kewan')
Simple_Controls.send_keys(Keys.RETURN)
Simple_Controls = driver.find_element(By.XPATH, '//*[@id="et_pb_contact_email_0"]')
Simple_Controls.click()
Simple_Controls.send_keys('kewan101@gmail.com')
Simple_Controls.send_keys(Keys.RETURN)
Simple_Controls = driver.find_element(By.XPATH, '//*[@id="et_pb_contact_form_0"]/div[2]/form/div/button')
Simple_Controls.click()

driver.quit()


#third-test
driver = webdriver.Chrome()
driver.get('https://ultimateqa.com/complicated-page')
buttons_count = len(driver.find_elements(By.XPATH, "//a[contains(text(), 'Button')]"))
print(f"there is {buttons_count} in this page")
if buttons_count == 12:
    print("test pass")
else:
    print("test fail")

driver.quit()
