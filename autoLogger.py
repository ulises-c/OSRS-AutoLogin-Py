# Retrieve Usernames and Passwords
from user_pass import user_pass_dict

import pyautogui as auto
import os
import time

username = 'testing1'
password = 'testing2'

os.system("open /Applications/RuneLite.app")

time.sleep(25)

auto.press('enter')
auto.write(username)
auto.press('enter')
auto.write(password)
auto.press('enter')