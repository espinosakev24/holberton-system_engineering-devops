#!/usr/bin/python3
""" exports to csv"""

import csv
import requests
from sys import argv

if __name__ == '__main__':
    URL = 'https://jsonplaceholder.typicode.com/'
    URL_USERS = URL + 'users/'
    user_id = requests.get(URL_USERS + argv[1]).json()['id']
    todos = requests.get(URL + 'todos').json()
    user = requests.get(URL_USERS + str(user_id)).json()
    filename = str(user_id) + '.csv'
    with open(filename, 'w') as fd:
        wr = csv.writer(fd, delimiter=',', quoting=csv.QUOTE_ALL)
        for task in todos:
            if task['userId'] == user.get('id'):
                wr.writerow([user.get('id'), user['name'],
                                 task['completed'], task['title']])
