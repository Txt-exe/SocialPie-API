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

def printCommands():
    print("\n -s : Start Spotify module to listen to artist and get plays")
    print("\n -f : Start Spotify module to follow artist of your choice")
    print("\n -p : Print The Combo List")
    print("\n -c : Set combolist")
    print("\n -q : quit program")

#gets combo list and stores 
def getCombo():
    list_num = int(input("How many combo list would you like to store?: "))

    list_inputP = list_num

    for x in range(list_num):
        
        list_input = input("Please enter the full path of the location of your combo list: ")
        loacation_used.append(list_input)


        #If file not found terminate program for safety reasons
        assert os.path.exists(list_input), "\nIFatal error did not find file at path, Closing..., "+str(list_input)

        f = open(list_input,'r+')
    print("\nStored Location")
    print("checking for duplicates and removing them...")
    time.sleep(2)
    print("Done\n")
    

    getCombo.combolist_l = set(loacation_used)

    #stuff you do with the file goes here
    f.close()


print('Welcome to Spoticry 2.0\n' )

print("-h for commands")

waitforin  = " "

while waitforin != '-q':
    waitforin = input(">: ")

    if waitforin == '-h':
        printCommands()
        

    elif waitforin == '-q':
        print("Exiting program...")
        time.sleep(2)
        clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        clearConsole()
        sys.exit()

    elif waitforin == '-c':
        getCombo()
    

        
    elif waitforin == '-p':
        print(combolist_l)
        

    

        """
    elif waitforin == '-s':
    
        for x in range(len(combolist_l)):
            chrome_options = Options()
            chrome_options.add_extension(r'E:\\Creator\\VPNcrx.crx')
            chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

            webdriver = driver.Chrome(options=chrome_options)
            spoticry.loadSpot(driver, combolist_l[x])
        """
        

    else:
        print("Unauthorized input\n")
        printCommands()


#print("Number of accounts in Combo List: ", len(acc))
#artistpage = input('Enter Profile Link: ')

#songLink = input('Enter Song Link: ')



#loadSpot(webdriver)
