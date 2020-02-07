#!/usr/bin/python3
import requests


def top_ten(subreddit):
    """ number of subscribers """
    user_agent = {'User-Agent': 'KevinEspinosa'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'limit': 10}
    req = requests.get(url, headers=user_agent, allow_redirects=False,
                       params=params)
    if req.status_code == 404:
        print('None')
        return
    dict_1 = req.json().get('data').get('children')
    for item in dict_1:
        print(item.get('data').get('title'))
