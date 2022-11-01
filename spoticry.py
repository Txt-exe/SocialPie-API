from progress import bar
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import csv
import random
import string

ArtistA = [

    # Kendrick Lamar
    'https://open.spotify.com/artist/2YZyLoL8N0Wb9xBt1NhZWg',

    # Jcole
    'https://open.spotify.com/artist/6l3HvQ5sa6mXTsMTB19rO5',

    # Joey Bad A$$
    'https://open.spotify.com/artist/2P5sC9cVZDToPxyomzF1UH',

    # 2Chains
    'https://open.spotify.com/artist/17lzZA2AlOHwCwFALHttmp',

    # Asap Ferg
    'https://open.spotify.com/artist/5dHt1vcEm9qb8fCyLcB3HL',

    # Kid Cudi
    'https://open.spotify.com/artist/0fA0VVWsXO9YnASrzqfmYu',

    # Childish Gambino
    'https://open.spotify.com/artist/73sIBHcqh3Z3NyqHKZ7FOL',

    # Travis Scott
    'https://open.spotify.com/artist/0Y5tJX1MQlPlqiwlOH1tJY',

    # Young Nudy
    'https://open.spotify.com/artist/5yPzzu25VzEk8qrGTLIrE1',

    # Tyga
    'https://open.spotify.com/artist/5LHRHt1k9lMyONurDHEdrp',

    # YG
    'https://open.spotify.com/artist/0A0FS04o6zMoto8OKPsDwY',

    # SBQ
    'https://open.spotify.com/artist/5IcR3N7QB1j6KBL8eImZ8m',

    # Future
    'https://open.spotify.com/artist/1RyvyyTE3xzB2ZywiAwp0i',

    # Tyler The Creator
    'https://open.spotify.com/artist/4V8LLVI7PbaPR0K2TGSxFF',

    # FredG
    'https://open.spotify.com/artist/0Y4inQK6OespitzD6ijMwb',

    # Asap Rocky
    'https://open.spotify.com/artist/13ubrt8QOOCPljQ2FL1Kca',

    # Vince Staples
    'https://open.spotify.com/artist/68kEuyFKyqrdQQLLsmiatm',

    # FBZ
    'https://open.spotify.com/artist/1dqGS5sT6PE2wEvP1gROZC',

    # JID
    'https://open.spotify.com/artist/6U3ybJ9UHNKEdsH7ktGBZ7',
]

all_drivers = []
global min_time_to_play
global max_time_to_play

# Class for Spoticry Module
class Spoticry:

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

    @staticmethod
    def load_spot():
        print("grabbing accounts")


        # Goes through accounts until all are used

        x = len(acc)
        for x in range(len(acc)):
            pass
            # Logs in to Spotify
            print(" Logging in with: ", acc[x])
            all_drivers[x].get(
                "https://accounts.spotify.com/en/login?continue=https%3A%2F%2Fopen.spotify.com%2F")
            time.sleep(5.0)
            testb = all_drivers[x].find_element(
                'xpath', '//*[@id="login-username"]')
            testb.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
            time.sleep(2)
            testb.send_keys(acc[x])
            testbc = all_drivers[x].find_element(
                "xpath", '//*[@id="login-password"]')
            testbc.send_keys(passwrd[x])
            testa = all_drivers[x].find_element("xpath", '//*[@id="login-button"]')
            time.sleep(4)
            testa.click()
            time.sleep(5)

    def play_song(songlink):

        x = len(acc)
        for x in range(len(acc)):
            # Gets Desired Track
            all_drivers[x].get(songlink)
            print("Logged in")
            time.sleep(9)
            # Closes trust function window
            testu = all_drivers[x].find_element(
                "xpath", '//*[@id="onetrust-close-btn-container"]/button')
            testu.click()
            time.sleep(random.randint(2, 5))
            # Plays Desired Track
            playbutton = all_drivers[x].find_element("xpath",
                                                     '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[3]/div[4]/div/div/div/div/div/button')
            playbutton.click()
            # Turns on repeat
            repeat = all_drivers[x].find_element("xpath",
                                                 '//*[@id="main"]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/div[2]/button[2]')
            repeat.click()
            time.sleep(random.randint(2, 4))
            repeat = all_drivers[x].find_element("xpath",
                                                 '//*[@id="main"]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/div[2]/button[2]')
            repeat.click()

    def play_random_song(songlink):

            x = len(acc)
            # Get Random Artist to play
            print('Playing Random Artist to play based off selection...')
            all_drivers[x].get(random.choice(ArtistA))
            time.sleep(4)
            randomplay = all_drivers[x].find_element("xpath",
                                                '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div/div[2]/div[2]/div[4]/div/div/div/div/div/button')
            randomplay.click()
            time.sleep(3)
            randomnize = all_drivers[x].find_element("xpath",
                                                '/html/body/div[4]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/div[1]/button[1]')
            randomnize.click()
            # Time to play artist randomly
            time.sleep(random.randint(60, 70))
            print("Playing Another Artist")
            all_drivers[x].get(random.choice(ArtistA))
            time.sleep(random.randint(5, 7))
            randomplay = all_drivers[x].find_element("xpath",
                                                '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div/div[2]/div[2]/div[4]/div/div/div/div/div/button')
            randomplay.click()
            time.sleep(3)
            # Time to play artist randomly
            time.sleep(random.randint(60, 80))
            # Reverse Back to Song
            print("Playing your song again...")
            all_drivers[x].get(songlink)
            time.sleep(9)
            playbutton = all_drivers[x].find_element("xpath",
                                                '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[3]/div[4]/div/div/div/div/div/button')
            playbutton.click()
            time.sleep(random.randint(min_time_to_play, max_time_to_play))
            print("Done, Logging out...")
            all_drivers[x].get(
                'https://www.spotify.com/us/account/overview/?utm_source=spotify&utm_medium=menu&utm_campaign=your_account')
            time.sleep(3)
            logout = all_drivers[x].find_element("xpath",
                                            '//*[@id="__next"]/div/div/div[2]/div[3]/div[2]/div/div[2]/article/div[2]/a')
            logout.click()
            print("Logged out")
            time.sleep(2)
            # clear cookies before starting a new account
            all_drivers[x].delete_all_cookies()
            time.sleep(2)

