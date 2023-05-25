#!/usr/bin/python3
"""
Exports all tasks from all employees to JSON format
"""
import json
import requests


def export_data_to_json():
    users_response = requests.get('https://jsonplaceholder.typicode.com/users')
    tasks_response = requests.get('https://jsonplaceholder.typicode.com/todos')

    users = users_response.json()
    tasks = tasks_response.json()

    user_tasks = {}

    for user in users:
        user_id = user['id']
        username = user['username']
        user_tasks[user_id] = []

        for task in tasks:
            if task['userId'] == user_id:
                task_data = {
                    'username': username,
                    'task': task['title'],
                    'completed': task['completed']
                }
                user_tasks[user_id].append(task_data)

    with open('todo_all_employees.json', 'w') as file:
        json.dump(user_tasks, file)


if __name__ == '__main__':
    export_data_to_json()
