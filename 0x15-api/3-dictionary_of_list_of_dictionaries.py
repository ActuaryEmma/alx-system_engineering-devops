#!/usr/bin/python3
"""export data in the JSON format for specific employee"""
import csv
import json
import sys
import urllib.request


if __name__ == "__main__":
    url = f"https://jsonplaceholder.typicode.com/users"
    url2 = f"https://jsonplaceholder.typicode.com/todos"
    # open and fetch data
    with urllib.request.urlopen(url) as f:
        data = json.loads(f.read().decode('utf-8'))
    with urllib.request.urlopen(url2) as f:
        data2 = json.loads(f.read().decode('utf-8'))
    json_file = "todo_all_employees.json.json"

    user_tasks = {}
    # iterate through each user and extracts username and ID
    for user in data:
        user_id = user['id']
        username = user['username']
        user_tasks[user_id] = []

        for task in data2:
            if task['userId'] == user_id:
                user_tasks[user_id].append({
                    "username": username,
                    "task": task['title'],
                    "completed": task['completed']
                })

    with open(json_file, "w") as file:
        json.dump(user_tasks, file)
