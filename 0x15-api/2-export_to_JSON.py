#!/usr/bin/python3
import json
import requests
from sys import argv

if __name__ == '__main__':
    URL = 'https://jsonplaceholder.typicode.com/'
    dict_file, records = {}, []
    done, total = 0, 0
    tasks_done = []
    URL_TODO = URL + 'todos/' + argv[1]
    URL_USERS = URL + 'users/'
    todos = requests.get(URL + 'todos').json()
    user_id = requests.get(URL_TODO).json().get('id')
    user = requests.get(URL_USERS + str(user_id)).json()

    for task in todos:
        if task.get('userId') == user_id:
            total += 1
            if task.get('completed'):
                tasks_done.append(task['title'])
                done += 1

    for task in todos:
        if task['userId'] == user_id:
            records.append({"task": task.get('title'),
                            "completed": task.get('completed'),
                            "username": user.get("username")})
    dict_file.update({str(user_id): records})

    filename = str(user_id) + '.json'
    with open(filename, 'w', encoding="utf-8") as jsonfile:
        jsonfile.write(json.dumps(dict_file))
