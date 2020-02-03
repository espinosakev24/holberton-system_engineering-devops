#!/usr/bin/python3
import requests
from sys import argv
import csv

if __name__ == '__main__':
    URL = 'https://jsonplaceholder.typicode.com/'
    URL_USERS = URL + 'users/'
    records, list_records = [], []
    user_id = requests.get(URL_USERS + argv[1]).json()['id']
    todos = requests.get(URL + 'todos').json()
    user = requests.get(URL_USERS + str(user_id)).json()
    filename = str(user_id) + '.csv'
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            if task['userId'] == user.get('id'):
                writer.writerow([user.get('id'), user['name'], task['completed'], task['title']])
            