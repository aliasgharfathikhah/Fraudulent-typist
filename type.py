from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
import sys


def type(str):
    for i in range(len(str)):
        time.sleep(.09)
        print(str[i], end='')
        sys.stdout.flush()
    print()

def getinfo():
    print("----------------------------")
    type("Hello, let me type for you (⌐■_■)")
    print("----------------------------")
    type("your emai (☞ﾟヮﾟ)☞ ")
    email = input()
    print("----------------------------")
    type("your password (☞ﾟヮﾟ)☞ ")
    password = input()
    return email, password

def login(email, password):
    driver.get('https://typetest.io/login/')
    driver.implicitly_wait(2)
    input_email = driver.find_element(By.ID, 'email')
    input_email.send_keys(email)
    input_password = driver.find_element(By.ID, 'password')
    input_password.send_keys(password)
    btn_login = driver.find_element(By.CLASS_NAME, 'button-highlight')
    btn_login.click()

def start_type():
    while True:
        try:
            chars = driver.find_elements(By.CLASS_NAME, 'test-char')

            input_field = driver.find_element(By.ID, 'test-input')

            for char in chars:
                time.sleep(.07)
                input_field.send_keys(char.text)
        except:
            print("ERROR!")

email, password = getinfo()
options = Options()
options.headless = False
driver = webdriver.Firefox(options=options)
driver.implicitly_wait(2)
login(email, password)
start_type()

