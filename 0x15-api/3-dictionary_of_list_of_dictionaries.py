#!/usr/bin/python3
"""dict list of dicts """
import json
import requests
from sys import argv

if __name__ == '__main__':
    URL = 'https://jsonplaceholder.typicode.com/'
    idx = 1
    dict_file, records = {}, []
    user_dict = {}
    URL_TODO = URL + 'todos/'
    URL_USERS = URL + 'users/'
    todos = requests.get(URL_TODO).json()
    users = requests.get(URL_USERS)

    while idx <= 10:
        task_user = requests.get(URL_TODO + '?userId=' + str(idx)).json()
        userResponse = requests.get(URL_USERS + str(idx)).json()
        for task in task_user:
            records.append({"task": task['title'], "completed":
                            task['completed'],
                            "username": userResponse['username']})
        user_dict.update({str(idx): records})
        idx += 1

    filename = "todo_all_employees.json"
    with open(filename, 'w', encoding="utf-8") as jsonfile:
        jsonfile.write(json.dumps(user_dict))
