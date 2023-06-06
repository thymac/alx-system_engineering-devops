#!/usr/bin/python3
"""
A recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], n=0, after=None):
    """Queries the Reddit API and returns a list containing the titles of
    all hot articles for a given subreddit.

    The Reddit API uses pagination for separating pages of responses.
    If not a valid subreddit, return None.

    Args:
        subreddit (str): Subreddit.
        hot_list (list, optional): List of titles. Defaults to [].
        n (int, optional): Counter for recursion depth. Defaults to 0.
        after (str, optional): Pagination token. Defaults to None.

    Returns:
        list: List of titles.
    """

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Custom User Agent'}
    params = {'limit': 100, 'after': after} if after else {'limit': 100}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title']
            hot_list.append(title)

        after = data['data']['after']
        if after is not None:
            recurse(subreddit, hot_list, n + 1, after)
        elif n == 0:
            return hot_list
    else:
        return None

    if n == 0:
        return hot_list

