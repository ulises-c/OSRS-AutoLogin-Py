""" Used to retrieve usernames and passwords """
from dotenv import load_dotenv
import os
load_dotenv('.env')

user_pass_dict = {}
user_list = []

main_user = os.getenv('main_user')
user_list.append(main_user)
user_pass_dict[main_user] = os.getenv('main_pass')

alt_user = os.getenv('alt_user')
user_pass_dict[alt_user]=os.getenv('alt_pass')
user_list.append(alt_user)

iron_user = os.getenv('iron_user')
user_pass_dict[iron_user]=os.getenv('iron_pass')
user_list.append(iron_user)

"""
To use this create a file called '.env'
Format the file like this:

main_user = 'username1'
main_pass = 'password1'

alt_user = 'username2'
alt_pass = 'password2'

iron_user = 'username3'
iron_pass = 'password3'
"""