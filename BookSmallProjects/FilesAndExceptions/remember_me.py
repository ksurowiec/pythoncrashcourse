import json
from collections import OrderedDict


user_info = {}
users = {}

print('\nPlease provide the details about yourself, enter \'q\' to quit.')

while True:
    user_info['username'] = input('What is your name: ')

    if user_info['username'] in users.keys():
        print('Sorry, the username already exists, please choose different one.')
        continue

    user_info['email'] = input('Provide your email: ')
    user_info['first_name'] = input('Please provide your first name: ')
    user_info['last_name'] = input('Please provide your last name: ')
    users[user_info['username']] = dict(user_info)

    with open('users.json', mode='w') as file_writer:
        json.dump(users, file_writer)

    add_another = input(
        'Do you want to add another person? (Type \'yes\' to continue or \'no\' to quit): ')
    if add_another == 'no':
        print('Good bye, thank you.')
        break
