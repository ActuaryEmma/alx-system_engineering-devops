#!/usr/bin/python3
"""export data in the JSON format for specific employee"""
import csv
import json
import sys
import urllib.request


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <id>")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print(f"Error: {sys.argv[1]} should be an integer")
        sys.exit(1)
    url = f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}"
    url2 = f"https://jsonplaceholder.typicode.com/todos?userId={sys.argv[1]}"
    with urllib.request.urlopen(url) as f:
        data = json.loads(f.read().decode('utf-8'))
    with urllib.request.urlopen(url2) as f:
        data2 = json.loads(f.read().decode('utf-8'))

    # completed = [],, loop through t in data2 check if completed is True,
    # it is append title to completed list
    completed = [t['title'] for t in data2 if t['completed']]

    # json_file = f"{sys.argv[1]}.json"
    # header = ["userId", "username", "completed", "title"]

	# with open(json_file, "w") as file:
		# usrname = data["username"]
        # Write the data rows
		# for t in data2:
        # json.dump({sys.argv[1]: [{"task": t['title'], "completed": t['completed'], "username": usrname}]})
    completed_tasks = []
    for t in data2:
        completed_tasks.append({
            "task": t['title'],
            "completed": t['completed'],
            "username": data["username"]
        })

    json_file = f"{sys.argv[1]}.json"

    with open(json_file, "w") as file:
        json.dump(completed_tasks, file, indent=4)
