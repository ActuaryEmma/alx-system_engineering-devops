#!/usr/bin/python3
"""export data in the JSON format for specific employee"""
import csv
import json
import sys
import urllib.request


if __name__ == "__main__":
    url = f"https://jsonplaceholder.typicode.com/users/"
    url2 = f"https://jsonplaceholder.typicode.com/todos/"
    with urllib.request.urlopen(url) as f:
        data = json.loads(f.read().decode('utf-8'))
    with urllib.request.urlopen(url2) as f:
        data2 = json.loads(f.read().decode('utf-8'))
    json_file = "todo_all_employees.json.json"

    user_tasks = {}
    for user in users_data:
        user_id = user['id']
        username = user['username']
        user_tasks[user_id] = []

        for task in todos_data:
            if task['userId'] == user_id:
                user_tasks[user_id].append({
                    "task": task['title'],
                    "completed": task['completed'],
                    "username": username
                })

    with open(json_file, "w") as file:
        json.dump(user_tasks, file, indent=4)
