#!/usr/bin/python3
"""
Python script that, using a REST API, retrieves and displays information
about the TODO list progress of a given employee ID.
"""

import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) < 2:
        exit()

    employee_id = argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    # Get the employee's information
    user_url = f"{base_url}/users/{employee_id}"
    response = requests.get(user_url)
    user_data = response.json()
    employee_username = user_data.get("username")

    # Get the employee's TODO tasks
    todo_url = f"{base_url}/todos?userId={employee_id}"
    response = requests.get(todo_url)
    todo_data = response.json()

    # Count the number of completed tasks and total tasks
    completed_tasks = [task for task in todo_data if task.get("completed")]
    total_tasks = len(todo_data)

    # Display the employee TODO list progress
    print(f"Employee {employee_username} is done with tasks "
          f"({len(completed_tasks)}/{total_tasks}):")

    # Display the title of completed tasks
    for task in completed_tasks:
        task_title = task.get("title")
        print(f"\t{task_title}")

