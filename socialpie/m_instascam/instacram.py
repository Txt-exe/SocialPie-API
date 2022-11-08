import csv
import random
import string
import time
from os import path

import pyperclip
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

temp_email = "https://temp-mail.org/en/view/6369aadcff35fd00f95e17ab"
password = ''.join(random.choice(string.ascii_letters) for i in range(10))

namess = "C:\\Users\\Chiave\\PycharmProjects\\social-api-data\\d_instacram\\names\\first_names.csv"


def create_accounts(first_namess):


    with open(first_namess,
              newline='') as f:
        reader = csv.reader(f)
        names = list(reader)
    chrome_options = Options()
    chrome_options.add_experimental_option(
        "excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=chrome_options)

    driver.get(temp_email)
    time.sleep(10)
    try:
        copy_button = driver.find_element('xpath', '//*[@id="mail"]')
    except NoSuchElementException:
        driver.quit()
    copy_button.click()
    copy_button.send_keys(Keys.CONTROL, 'c')
    time.sleep(2)
    driver.get("https://www.instagram.com/accounts/emailsignup/")
    time.sleep(7)

    try:
        email = driver.find_element(By.CSS_SELECTOR, "input[name='emailOrPhone']")
    except NoSuchElementException:
        driver.quit()

    time.sleep(3)
    email.send_keys(Keys.CONTROL, 'v')

    try:
        full_name = driver.find_element(By.CSS_SELECTOR, "input[name='fullName']")
    except NoSuchElementException:
        print("didn't find input[name='fullName']")
        driver.quit()

    time.sleep(2)
    full_name.send_keys(random.choice(names))
    time.sleep(3)

    try:
        username = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
    except NoSuchElementException:
        print("didn't find input[name='username']")
        driver.quit()
    username.send_keys(random.choice(names), random.randint(23548, 98544), random.choice(names))
    try:
        pswrd = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
    except NoSuchElementException:
        print("didn't find input[name='password']")
        driver.quit()
    pswrd.send_keys(password)
    time.sleep(2)

    email.send_keys(Keys.CONTROL, 'a')
    email.send_keys(Keys.CONTROL, 'c')

    if path.exists("accounts.txt") and path.isfile("accounts.txt"):
        s = pyperclip.paste()
        with open('accounts.txt', 'w') as g:
            g.write(s)

create_accounts(namess)
