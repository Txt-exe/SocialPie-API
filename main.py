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

print('Welcome to SocialPie 2.0\n')

print("-h for commands")


def print_commands():
    print("\n -ss : Start Spotify module to listen to artist and get plays")
    print("\n -sf : Start Spotify module to follow artist of your choice")
    print("\n -sp : Print The Combo List")
    print("\n -sa : Add a list of accounts")
    print("\n -q : quit program")
    print("\n -c : clear console")


# gets combo list and stores
def get_combo():
    list_num = input("How many combo list's would you like to store?: ")
    try:
        int(list_num)

    except:
        print("That's not an integer number.")
        main()
    else:
        for x in range(int(list_num)):
            list_input = input(
                "Please enter the full path of the location of your combo list: ")
            loacation_used.append(list_input)
            # If file not found delete entry and return to program
            if not (os.path.exists(list_input)):
                print("FILE NOT FOUND ")
                loacation_used.remove(list_input)
                main()
            f = open(list_input, )
    print("\nStored Location")
    print("checking for duplicates and removing them...")
    time.sleep(2)
    print("Done\n")

    f.close()


def clear_console():
    return os.system(
        'cls' if os.name in ('nt', 'dos') else 'clear')


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

            clear_console()
            sys.exit()

        elif waitforin == '-c':
            clear_console()

        elif waitforin == '-sa':
            get_combo()

        elif waitforin == '-sp':

            if (len(set(loacation_used)) == 0):
                print("I cant find any accounts right now...")
            else:

                print(set(loacation_used))

        elif waitforin == '-ss':

            if len(set(loacation_used)) == 0:
                print("There hasn't been any accounts added to the program")
            if len(set(loacation_used)) >= 1:

                min_time_to_play = int(input("what is the minimum (in minutes) would you like to play your song?: "
                                             "(Before switching accounts): "))
                try:
                    int(min_time_to_play)

                except:
                    print("That's not an integer number.")
                    main()
                max_time_to_play = int(input("what is the maximum (in minutes) would you like to play your song?"
                                             "(Before switching accounts): "))
                try:
                    int(max_time_to_play)

                except:
                    print("That's not an integer number.")
                    main()
                else:
                    min_con = min_time_to_play * 60
                    max_con = max_time_to_play * 60
                    get_song = input("Enter link to spotify song: ")
                    if "https://open.spotify.com/track" not in get_song:
                        print("This is not a spotify link, exiting...")
                        time.sleep(2)
                        main()
                    else:

                        print("Opening Spotify, Please wait...")
                        for x in range(len(set(loacation_used))):
                            spoticry.Spoticry.open_accounts(loacation_used)
                            spoticry.Spoticry.load_spot()
                            spoticry.Spoticry.play_song(
                                get_song)
        else:
            print("Value not recognized...")
            print_commands()


main()
