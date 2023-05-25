#!/usr/bin/python3
"""
Exports employee tasks to CSV format
"""

import csv
import requests
from sys import argv


def export_to_csv(employee_id):
    """
    Exports employee tasks to CSV file
    """
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
            employee_id)
    tasks_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            employee_id)

    user_response = requests.get(user_url)
    tasks_response = requests.get(tasks_url)

    user_data = user_response.json()
    tasks_data = tasks_response.json()

    employee_username = user_data.get('username')

    csv_filename = '{}.csv'.format(employee_id)

    with open(csv_filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for task in tasks_data:
            task_completed = task.get('completed')
            task_title = task.get('title')
            writer.writerow([employee_id, employee_username, task_completed,
                task_title])


if __name__ == '__main__':
    if len(argv) != 2:
        print('Usage: {} <employee_id>'.format(argv[0]))
        exit(1)

    employee_id = argv[1]
    export_to_csv(employee_id)
