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

    output = requests.get("https://www.reddit.com/r/{}/about.json"
                          .format(subreddit),
                          headers={"User-Agent": "My-User-Agent"},
                          allow_redirects=False)
    if output.status_code == 200:
        about_dict = output.json()
        return about_dict.get('data').get('subscribers')
    else:
        return 0
