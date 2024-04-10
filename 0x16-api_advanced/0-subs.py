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
    from config import reddit_access_token

    headers = {"User-Agent": "My-User-Agent"}
    headers['Authorization'] = f'bearer {reddit_access_token}'

    output = requests.get("https://oauth.reddit.com/r/{}/about.json"
                          .format(subreddit),
                          headers=headers,
                          allow_redirects=False)
    if output.status_code == 200:
        about_dict = output.json()
        return about_dict.get('data').get('subscribers')
    else:
        return 0
