#!/usr/bin/python3
"""
Python script that, using a given REST API,
returns information about an employee's TODO list progress.
"""
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) < 2:
        exit()

    employee_id = argv[1]
    base_url = 'https://jsonplaceholder.typicode.com'

    # Get employee name
    user_url = f'{base_url}/users/{employee_id}'
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Get employee's TODO list
    todos_url = f'{base_url}/todos?userId={employee_id}'
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Count completed tasks
    completed_tasks = [task for task in todos_data if task.get('completed')]
    num_completed_tasks = len(completed_tasks)
    total_num_tasks = len(todos_data)

    # Print progress information
    print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_num_tasks}):")

    # Print titles of completed tasks
    for task in completed_tasks:
        print(f"\t{task.get('title')}")

