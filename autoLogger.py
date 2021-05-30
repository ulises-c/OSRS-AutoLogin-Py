# Retrieve Usernames and Passwords
from user_pass import user_pass_dict

import pyautogui as auto

username = 'testing1'
password = 'testing2'

auto.write(username)
auto.press('enter')
auto.write(password)