from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.headless = False
driver = webdriver.Firefox(options=options)

driver.get('https://typetest.io/')


driver.implicitly_wait(4)
while True:
    driver.implicitly_wait(3)
    chars = driver.find_elements(By.CLASS_NAME, 'test-char')

    for char in chars:
        print(char.text, end='')

    input_field = driver.find_element(By.ID, 'test-input')

    for char in chars:
        input_field.send_keys(char.text)


