#!/usr/bin/python3
"""function that returns the number of subscribers for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Gets number of subscribers
       Args:
           subreddit (str): name of subreddit to query
       Returns:
           int: number of subscribers if valid, 0 if otherwise
    """
    base_url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyRedditBot/1.0'}
    response = requests.get(base_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        about_dict = response.json()
        return about_dict['data']['subscribers']
    else:
        return 0
