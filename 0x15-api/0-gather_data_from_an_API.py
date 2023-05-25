#!/usr/bin/python3
"""
Script that fetches information about a given employee's ID using an API.
"""

import json
import requests
import sys

base_url = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 script.py [employee_id]")
        sys.exit(1)

    employee_id = sys.argv[1]

    # Retrieve user information
    user_url = f'{base_url}/users?id={employee_id}'
    response = requests.get(user_url)
    data = response.json()

    if not data:
        print(f"No user found with ID: {employee_id}")
        sys.exit(1)

    user = data[0]
    employee_name = user.get('name')

    # Retrieve user's TODO tasks
    tasks_url = f'{base_url}/todos?userId={employee_id}'
    response = requests.get(tasks_url)
    tasks = response.json()

    # Count the number of completed tasks and total tasks
    completed_tasks = [task for task in tasks if task.get('completed')]
    completed_count = len(completed_tasks)
    total_tasks = len(tasks)


    for task in completed_tasks:
        task_title = task.get('title')
        print(f"\t{task_title}")
