#!/usr/bin/python3
"""dict list of dicts. """
import json
import requests
from sys import argv

if __name__ == '__main__':
    URL = 'https://jsonplaceholder.typicode.com/'
    records = []
    user_dict = {}
    URL_TODO = URL + 'todos/'
    URL_USERS = URL + 'users/'
    todos = requests.get(URL_TODO).json()
    users = requests.get(URL_USERS).json()

    for user in users:
        task_user = requests.get(URL_TODO + '?userId=' +
                                 str(user.get('id'))).json()
        userResponse = requests.get(URL_USERS + str(user.get('id'))).json()
        for task in task_user:
            records.append({"username": userResponse.get('username'),
                            "task": task.get('title'),
                            "completed": task.get('completed')})
        user_dict.update({str(user.get('id')): records})
        records = []

    filename = "todo_all_employees.json"
    with open(filename, 'w', encoding="utf-8") as jsonfile:
        json.dump(user_dict, jsonfile)
