#!/usr/bin/python3
"""Function that prints top ten hot posts for a given subreddit"""
import requests


def top_ten(subreddit):
    """Gets top ten posts in subreddit
       Args:
           subreddit (str): name of subreddit
    """
    CLIENT_ID = '4nnh-n-k10tN0YReY9iz9g'
    SECRET_KEY = '2dyvCWMw8dKRYq2cCPsxQiHWlwZO-Q'
    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)
    data = {
        'grant_type': 'password',
        'username': 'Acrobatic-Donut-9369',
        'password': 'gg438379AP!'
        }
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)
    TOKEN = res.json()['access_token']
    headers['Authorization'] = f'bearer {TOKEN}'
    url = f'https://oauth.reddit.com/r/{subreddit}/hot?limit=9'
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print('None')
    else:
        hot_dict = response.json()
        if len(hot_dict['data']['children']) == 0:
            print('None')
        else:
            for d in hot_dict['data']['children']:
                print(d['data']['title'])
