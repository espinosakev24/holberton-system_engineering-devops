#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """ number of subscribers """
    user_agent = {'User-Agent': 'KevinEspinosa'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    req = requests.get(url, headers=user_agent, allow_redirects=False).json()
    try:
        return req.get('data').get('subscribers')
    except Exception:
        return 0
