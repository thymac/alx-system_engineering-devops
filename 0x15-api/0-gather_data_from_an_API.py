#!/usr/bin/python3
"""
Script that fetches information about a given employee's ID using an API.
"""

import json
import requests
import sys

base_url = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":
    user_id = sys.argv[1]

    # Get user info
    user_url = f'{base_url}/users?id={user_id}'
    response = requests.get(user_url)
    data = response.json()

    # Check if user exists
    if not data:
        print(f"No user found with ID: {user_id}")
        sys.exit(1)

    name = data[0]['name']

    # Get user's TODO tasks
    tasks_url = f'{base_url}/todos?userId={user_id}'
    response = requests.get(tasks_url)
    tasks = response.json()

    completed_tasks = []
    for task in tasks:
        if task['completed']:
            completed_tasks.append(task)

    completed = len(completed_tasks)
    total_tasks = len(tasks)

    print(f"Employee {name} is done with tasks({completed}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

