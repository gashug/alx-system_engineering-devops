#!usr/bin/python3
"""Prints sorted count of given keywords on querying Reddit API"""

import requests
import re

def count_words(subreddit, word_list, after=None, results=None):
    if results is None:
        results = {}

    headers = {'User-Agent': 'my-app/0.0.1'}

    if after:
        params = {'after': after}
    else:
        params = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                word = word.lower()
                occurrences = len(re.findall(r'\b' + re.escape(word) + r'\b', title))
                if occurrences > 0:
                    if word in results:
                        results[word] += occurrences
                    else:
                        results[word] = occurrences

        if data['data']['after']:
            count_words(subreddit, word_list, data['data']['after'], results)
        else:
            print_results(results)
    else:
        print("Error: Unable to retrieve data from the subreddit.")

def print_results(results):
    sorted_results = sorted(results.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_results:
        print(f"{word}: {count}")

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        count_words(sys.argv[1], sys.argv[2].split())
import requests
import re

def count_words(subreddit, word_list, after=None, results=None):
    if results is None:
        results = {}

    headers = {'User-Agent': 'my-app/0.0.1'}

    if after:
        params = {'after': after}
    else:
        params = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                word = word.lower()
                occurrences = len(re.findall(r'\b' + re.escape(word) + r'\b', title))
                if occurrences > 0:
                    if word in results:
                        results[word] += occurrences
                    else:
                        results[word] = occurrences

        if data['data']['after']:
            count_words(subreddit, word_list, data['data']['after'], results)
        else:
            print_results(results)
    else:
        print("Error: Unable to retrieve data from the subreddit.")

def print_results(results):
    sorted_results = sorted(results.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_results:
        print(f"{word}: {count}")

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        count_words(sys.argv[1], sys.argv[2].split())
