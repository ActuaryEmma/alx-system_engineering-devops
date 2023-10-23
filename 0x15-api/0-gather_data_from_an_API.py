#!/usr/bin/python3
""" urllib.request - help in opening URLs mostly HTTP
    urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None,
    capath=None, cadefault=False, context=None)
"""

import urllib.request
import sys
import json
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
print("Employee {} is done with tasks({}/{}):".format(
        data["username"], len(completed), len(data2)))
# return title list of completed tasks
for c in completed:
    print("\t{}".format(c))
