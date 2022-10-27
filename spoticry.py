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
class Spoticry:

    def follow_artist(artistpage):
        # Follows Artist
        webdriver.get(artistpage)
        time.sleep(random.randint(3, 5))
        follow = webdriver.find_element_by_xpath(
            '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div/div[2]/div[2]/div[4]/div/div/div/div/button[1]')
        follow.click()
        time.sleep(3)


    # Loads All accounts from the combo list file
    def load_spot(webdriver, combo_list, songLink):
        print("grabbing accounts")
        with open(combo_list, "r") as f:
            accounts = [line.strip() for line in f]
        acc = [i.split(':')[0] for i in accounts]
        passwrd = [i.split(':')[1] for i in accounts]

        # Goes through accounts until all are used
        x = len(acc)
        for x in range(len(acc)):
            bar.next()
            pass


            # Logs in to Spotify
            print(" Logging in with: ", acc[x])
            webdriver.get("https://accounts.spotify.com/en/login?continue=https%3A%2F%2Fopen.spotify.com%2F")
            time.sleep(5.0)

            testb = webdriver.find_element_by_xpath('//*[@id="login-username"]')
            testb.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
            time.sleep(2)
            testb.send_keys(acc[x])
            testbc = webdriver.find_element_by_xpath('//*[@id="login-password"]')
            testbc.send_keys(passwrd[x])
            testa = webdriver.find_element_by_xpath('//*[@id="login-button"]')
            time.sleep(9)
            testa.click()

            time.sleep(5)

            # Gets Desired Track
            webdriver.get(songLink)

            time.sleep(5)

            # Closes trust function window
            testu = webdriver.find_element_by_xpath('//*[@id="onetrust-close-btn-container"]/button')
            testu.click()
            time.sleep(random.randint(2, 5))

            # Plays Desired Track
            playbutton = webdriver.find_element_by_xpath(
                '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[3]/div[4]/div/div/div/div/div/button')
            playbutton.click()

            # Turns on repeat
            repeat = webdriver.find_element_by_xpath(
                '//*[@id="main"]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/div[2]/button[2]')
            repeat.click()
            time.sleep(random.randint(2, 4))
            repeat.click()

            # Time to play song
            time.sleep(random.randint(4, 8))

            """
            search = webdriver.find_element_by_xpath('//*[@id="main"]/div/div[2]/nav/div[1]/ul/li[2]/a')
            search.click()
        
            look = webdriver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/header/div[3]/div/div/form/input')
            look.send_keys()
            """

            # Get Random Artist to play
            print('Playing Random Artist to play based off selection...')
            webdriver.get(random.choice(ArtistA))
            time.sleep(4)

            randomplay = webdriver.find_element_by_xpath(
                '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div/div[2]/div[2]/div[4]/div/div/div/div/div/button')
            randomplay.click()
            time.sleep(3)

            randomnize = webdriver.find_element_by_xpath(
                '/html/body/div[4]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/div[1]/button[1]')
            randomnize.click()

            # Time to play artist randomly
            time.sleep(random.randint(7, 10))

            print("Playing Another Artist")
            webdriver.get(random.choice(ArtistA))
            time.sleep(random.randint(5, 7))
            randomplay = webdriver.find_element_by_xpath(
                '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div/div[2]/div[2]/div[4]/div/div/div/div/div/button')
            randomplay.click()
            time.sleep(3)

            # Time to play artist randomly
            time.sleep(random.randint(7, 9))

            # Reverse Back to Song
            print("Playing your song again...")
            webdriver.get(songLink)

            playbutton = webdriver.find_element_by_xpath(
                '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[3]/div[4]/div/div/div/div/div/button')

            playbutton.click()
            time.sleep(random.randint(6, 8))

            print("Done, Logging out...")

            webdriver.get(
                'https://www.spotify.com/us/account/overview/?utm_source=spotify&utm_medium=menu&utm_campaign=your_account')
            time.sleep(3)
            logout = webdriver.find_element_by_xpath(
                '//*[@id="__next"]/div/div/div[2]/div[3]/div[2]/div/div[2]/article/div[2]/a')
            logout.click()
            print("Logged out")

            time.sleep(2)

            # clear cookies before starting a new account
            webdriver.delete_all_cookies()
            time.sleep(2)
