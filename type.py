from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.headless = False
driver = webdriver.Firefox(options=options)

driver.get('https://typetest.io/')


driver.implicitly_wait(2)
while True:
    try:
        chars = driver.find_elements(By.CLASS_NAME, 'test-char')

        input_field = driver.find_element(By.ID, 'test-input')

        for char in chars:
            input_field.send_keys(char.text)
            
    except:
        print("ERROR!")


