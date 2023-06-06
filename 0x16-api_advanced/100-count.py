#!/usr/bin/python3
"""
count.py
"""

import requests


def count_words(subreddit, word_list, hot_list=[], after=None):
    """
    Recursively queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords.

    If word_list contains the same word (case-insensitive), the final count
    should be the sum of each duplicate. Results are printed in descending
    order by the count, and if the count is the same for separate keywords,
    they are sorted alphabetically (ascending).

    Args:
        subreddit (str): The subreddit to search for.
        word_list (list): List of keywords to count occurrences for.
        hot_list (list): The list to store the titles of hot articles. (default=[])
        after (str): Token for pagination. (default=None)

    Returns:
        None
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Custom User Agent'}
    params = {'limit': 100, 'after': after} if after else {'limit': 100}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title'].lower()
            hot_list.append(title)

        after = data['data']['after']
        if after is not None:
            count_words(subreddit, word_list, hot_list=hot_list, after=after)
        else:
            count_occurrences(word_list, hot_list)
    else:
        print("None")


def count_occurrences(word_list, hot_list):
    """
    Counts the occurrences of keywords in the hot_list and prints the results.

    Args:
        word_list (list): List of keywords to count occurrences for.
        hot_list (list): List containing the titles of hot articles.

    Returns:
        None
    """
    word_count = {word: 0 for word in word_list}

    for title in hot_list:
        for word in word_list:
            if word.lower() in title:
                word_count[word] += 1

    sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_words:
        print(word + ": " + str(count))
