from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import csv
import random
from progress.bar import ShadyBar
import string
import sys
import os
import time
import spoticry

loacation_used = []

print('Welcome to Spoticry 2.0\n')

print("-h for commands")


def print_commands():
    print("\n -s : Start Spotify module to listen to artist and get plays")
    print("\n -f : Start Spotify module to follow artist of your choice")
    print("\n -p : Print The Combo List")
    print("\n -c : Set combolist")
    print("\n -q : quit program")


# gets combo list and stores
def get_combo():
    list_num = input("How many combo list would you like to store?: ")
    try:
        int(list_num)

    except:
        print("That's not an integer number.")
        main()
    else:
        for x in range(int(list_num)):
            list_input = input("Please enter the full path of the location of your combo list: ")
            loacation_used.append(list_input)

            # If file not found terminate program for safety reasons
            print(os.path.exists(list_input), "\nFatal error did not find file at path " + str(
              list_input))
            main()
            f = open(list_input, )
    print("\nStored Location")
    print("checking for duplicates and removing them...")
    time.sleep(2)
    print("Done\n")

    f.close()


def main():

    waitforin = " "
    waitforin.strip()

    while waitforin != '-q':
        waitforin = input(">: ")

        if waitforin == '-h':

            print_commands()


        elif waitforin == '-q':
            print("Exiting program...")
            time.sleep(2)
            clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
            clearConsole()
            sys.exit()

        elif waitforin == '-c':
            get_combo()



        elif waitforin == '-p':

            if (len(set(loacation_used)) == 0):
                print("I cant find any accounts right now...")
            else:

                print(set(loacation_used))

        elif waitforin == '-s':

            if len(set(loacation_used)) == 0:
                print("There hasn't been any accounts added to the program")
            for x in range(len(set(loacation_used))):
                chrome_options = Options()
                chrome_options.add_extension(r'C:\Users\Chiave\PycharmProjects\Spoticry\VPNcrx.crx')
                chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

                driver = webdriver.Chrome(options=chrome_options)
                spoticry.Spoticry.load_spot(driver, set(loacation_used),
                                            "https://open.spotify.com/track/12HLq6Udogz52kh7Rj3FMg?si=f926d06b2fdc489c")
        else:
            print("Value not recognized...")
            print_commands()

main()