# Retrieve Usernames and Passwords
from user_pass import user_pass_dict as passwords
from user_pass import user_list as usernames

import pyautogui as auto
import os
import time

# Open RuneLite on macOS
os.system('open /Applications/RuneLite.app')

# Sleep to let RuneLite load
time.sleep(30)

# To enter login screen
auto.press('enter')

# To write user name
auto.write(usernames[0])
auto.press('enter')

# To write password
auto.write(passwords[usernames[0]])
auto.press('enter')