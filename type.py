from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By


email = input("your emai-> ")
password = input("your password-> ")

options = Options()
options.headless = False
driver = webdriver.Firefox(options=options)

driver.get('https://typetest.io/login')

driver.implicitly_wait(2)

input_email = driver.find_element(By.ID, 'email')
input_email.send_keys(email)

input_password = driver.find_element(By.ID, 'password')
input_password.send_keys(password)

btn_login = driver.find_element(By.CLASS_NAME, 'button-highlight')
btn_login.click()

driver.implicitly_wait(2)
while True:
    try:
        chars = driver.find_elements(By.CLASS_NAME, 'test-char')

        input_field = driver.find_element(By.ID, 'test-input')

        for char in chars:
            input_field.send_keys(char.text)
            
    except:
        print("ERROR!")


