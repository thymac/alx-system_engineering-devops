#!/usr/bin/python3
"""
Python script that, using a given REST API,
returns information about an employee's TODO list progress.
"""

import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: {} employee_id".format(argv[0]))
        exit(1)

    employee_id = argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/{}".format(base_url, employee_id)
    todos_url = "{}/todos?userId={}".format(base_url, employee_id)

    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)
        employee_name = user_response.json().get('name')
        todos = todos_response.json()
    except Exception as e:
        print("Error: {}".format(e))
        exit(1)

    completed_tasks = [task for task in todos if task.get('completed')]
    total_tasks = len(todos)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_tasks), total_tasks
    ))

    for task in completed_tasks:
        print("\t{}".format(task.get('title')))

