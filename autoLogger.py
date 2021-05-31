# Retrieve Usernames and Passwords
from user_pass import user_pass_dict as passwords
from user_pass import user_list as usernames
from checkRunning import rl_running

import pygetwindow as gw
import pyautogui as auto
import os
import time

macRuneLite = '/Applications/RuneLite.app'

def choose_user(user_list):
    print('\nList of usernames:')
    for i in range(len(user_list)):
        print("{}: {}".format(i, user_list[i]))
    entry = (int)(input('\nEnter the number of the user you want to log into: '))
    print("Selected: {}, {}".format(entry, user_list[entry]))
    return user_list[entry]

def activate_runelite(rl_status):
    if(not rl_status):
        # Open RuneLite on macOS, if already open it brings the window to the front
        os.system('open ' + macRuneLite)

        # Sleep to let RuneLite load
        time.sleep(20)

    elif(rl_status):
        os.system('open ' + macRuneLite)

def login(username, password):
    # To enter login screen
    auto.press('enter')

    # To write user name
    auto.write(username)
    auto.press('enter')

    # To write password
    auto.write(password)
    auto.press('enter')

""" MAIN """

username = choose_user(usernames)
activate_runelite(rl_running)
login(username, passwords[username])