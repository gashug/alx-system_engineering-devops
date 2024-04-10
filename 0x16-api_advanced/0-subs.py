#!/usr/bin/python3
"""function that returns the number of subscribers for a given subreddit"""


def number_of_subscribers(subreddit):
    """Gets number of subscribers
       Args:
           subreddit (str): name of subreddit to query
       Returns:
           int: number of subscribers if valid, 0 if otherwise
    """
    import requests

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
    url = f'https://oauth.reddit.com/r/{subreddit}/about'
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        about_dict = response.json()
        return about_dict['data']['subscribers']
    else:
        return 0
