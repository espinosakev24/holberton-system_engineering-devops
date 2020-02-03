#!/usr/bin/python3
import requests
from sys import argv

if __name__ == '__main__':
    URL = 'https://jsonplaceholder.typicode.com/'
    done, total = 0, 0
    tasks_done = []
    URL_TODO = URL + 'todos/' + argv[1]
    URL_USERS = URL + 'users/'
    todos = requests.get(URL + 'todos').json()
    user_id = requests.get(URL_TODO).json().get('id')
    user = requests.get(URL_USERS + str(user_id)).json()
    employee_name = user['name']
    for task in todos:
        if task['userId'] == user_id:
            total += 1
            if task['completed']:
                tasks_done.append(task['title'])
                done += 1
    print("Employee {} is done with tasks({}/{}):".
          format(employee_name, done, total))
    for task in tasks_done:
        print("\t {}".format(task))
