# Retrieve Usernames and Passwords
from user_pass import user_pass_dict as passwords
from user_pass import user_list
from user_pass import alias_list
import checkRunning

# import pygetwindow as gw # May be used in Windows, not useful in macOS
import pyautogui as auto

def choose_user(usernames, aliases):
    print('\nList of usernames:')
    for i in range(len(aliases)):
        print("{}: {}".format(i, aliases[i]))
    entry = (int)(input('\nEnter the number of the user you want to log into: '))
    print("Selected: {}, {}".format(entry, aliases[entry]))
    return usernames[entry]

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

username = choose_user(user_list, alias_list)
checkRunning.activate_runelite() # Only for macOS
login(username, passwords[username])