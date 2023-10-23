#!/usr/bin/python3
"""export data in the CSV format"""
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

    csv_file = f"{sys.argv[1]}.csv"
    # header = ["userId", "username", "completed", "title"]

    with open(csv_file, "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        # Write the header row
        # writer.writerow(header)
        usrname = data["username"]
        # Write the data rows
        for t in data2:
            writer.writerow([sys.argv[1], usrname, t['completed'], t['title']])
