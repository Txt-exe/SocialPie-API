from progress import bar
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import csv
import random

# Driver array
all_drivers = []


def get_artist(artist_file):
    with open(artist_file, newline='') as f:
        reader = csv.reader(f)
        global artist_a
        artist_a = list(reader)


# Opens list of accounts and creates windows based off number of lines
def open_accounts(accounts):
    global acc
    global passwrd

    for i in accounts:
        with open(i, "r") as f:

            accounts = [line.strip() for line in f]
            acc = [i.split(':')[0] for i in accounts]
            passwrd = [i.split(':')[1] for i in accounts]
        chrome_options = Options()
        chrome_options.add_experimental_option(
            "excludeSwitches", ["enable-logging"])
        for n in acc:
            driver = webdriver.Chrome(options=chrome_options)
            all_drivers.append(driver)


# logs in to Spotify using accounts list
def load_spot():
    print("grabbing accounts")
    x = len(acc)
    for x in range(len(acc)):
        pass
        # Logs in to Spotify
        print(" Logging in with: ", acc[x], "in browser number", all_drivers[x])
        all_drivers[x].get(
            "https://accounts.spotify.com/en/login?continue=https%3A%2F%2Fopen.spotify.com%2F")
        all_drivers[x].implicitly_wait(5)

        try:
            testb = all_drivers[x].find_element(
                'xpath', '//*[@id="login-username"]')
        except NoSuchElementException:
            print("Cant Find element closing")
            all_drivers[x].quit()

        testb.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
        time.sleep(2)
        testb.send_keys(acc[x])

        try:
            testbc = all_drivers[x].find_element(
                "xpath", '//*[@id="login-password"]')
        except NoSuchElementException:
            print("Cant Find element closing")
            all_drivers[x].quit()

        testbc.send_keys(passwrd[x])

        try:
            testa = all_drivers[x].find_element("xpath", '//*[@id="login-button"]')
        except NoSuchElementException:
            time.sleep(4)
            all_drivers[x].quit()

        testa.click()
        print("Logged in")
        time.sleep(5)
        if (all_drivers[x].current_url == "https://accounts.spotify.com/en/login?continue=https%3A%2F%2Fopen.spotify"
                                          ".com%2F"):
            all_drivers[x].refresh()
            print("Log in not found...quiting")
            time.sleep(3)
            all_drivers[x].quit()


        else:
            continue


# Plays specific song [takes link as parameter]
def play_song(songlink):
    x = len(acc)
    for x in range(len(acc)):
        # Gets Desired Track
        all_drivers[x].get(songlink)
        print("Found track")
        time.sleep(9)
        # Closes trust function window
        testu = all_drivers[x].find_element(
            "xpath", '//*[@id="onetrust-close-btn-container"]/button')
        testu.click()
        time.sleep(random.randint(2, 5))
        try:
            # Plays Desired Track
            playbutton = all_drivers[x].find_element("xpath",
                                                     '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[3]/div[4]/div/div/div/div/div/button')
        except NoSuchElementException:
            all_drivers[x].close()
        playbutton.click()
        print("Playing")

        # Turns on repeat
        repeat = all_drivers[x].find_element("xpath",
                                             '//*[@id="main"]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/div[2]/button[2]')
        repeat.click()
        time.sleep(random.randint(2, 4))
        repeat = all_drivers[x].find_element("xpath",
                                             '//*[@id="main"]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/div[2]/button[2]')
        repeat.click()


# Plays random song to throw off algorithm
def play_random_song():
    x = len(acc)
    for x in range(len(acc)):
        print('Playing Random Artist to play based off selection...')
        all_drivers[x].get(random.choice(artist_a))
        time.sleep(4)
        randomplay = all_drivers[x].find_element("xpath",
                                                 '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div/div[2]/div[2]/div[4]/div/div/div/div/div/button')
        randomplay.click()
        time.sleep(3)
        randomnize = all_drivers[x].find_element("xpath",
                                                 '/html/body/div[4]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/div[1]/button[1]')
        randomnize.click()
        # Time to play artist randomly


def quit_browser():
    x = len(acc)
    all_drivers[x].quit()
