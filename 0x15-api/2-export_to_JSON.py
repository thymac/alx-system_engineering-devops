#!/usr/bin/python3
"""
Python script that fetches information about a given employee using an API
and exports the data in JSON format.
"""

import json
import requests
import sys


base_url = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":
    user_id = sys.argv[1]

    # Get user info from API
    user_url = f"{base_url}/users?id={user_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    username = user_data[0].get('username')

    # Get user's todo tasks from API
    tasks_url = f"{base_url}/todos?userId={user_id}"
    tasks_response = requests.get(tasks_url)
    tasks = tasks_response.json()

    # Build the JSON data
    json_data = {user_id: []}
    for task in tasks:
        json_data[user_id].append({
            "task": task['title'],
            "completed": task['completed'],
            "username": username
        })

    # Write JSON data to file
    with open(f"{user_id}.json", 'w') as json_file:
        json.dump(json_data, json_file)
