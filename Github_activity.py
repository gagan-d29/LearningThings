import sys
import json
from urllib.request import urlopen


# Check whether username was provided
if len(sys.argv) < 2:
    print("Usage: python Github_activity.py <username>")
    sys.exit()


# Get username from command line
username = sys.argv[1]

# Create GitHub API URL
url = f"https://api.github.com/users/{username}/events"

# Send request to GitHub
response = urlopen(url)

# Read and convert JSON data into Python
data = json.loads(response.read().decode())


# Display recent activity
print(f"\nRecent GitHub activity for {username}:\n")

for event in data:

    event_type = event["type"]
    repo = event["repo"]["name"]

    if event_type == "PushEvent":
        commits = len(event["payload"].get("commits", []))
        print(f"- Pushed {commits} commit(s) to {repo}")

    elif event_type == "IssuesEvent":
        action = event["payload"]["action"]
        print(f"- {action.capitalize()} an issue in {repo}")

    elif event_type == "PullRequestEvent":
        action = event["payload"]["action"]
        print(f"- {action.capitalize()} a pull request in {repo}")

    elif event_type == "WatchEvent":
        print(f"- Starred {repo}")

    elif event_type == "ForkEvent":
        print(f"- Forked {repo}")

    elif event_type == "CreateEvent":
        print(f"- Created something in {repo}")

    else:
        print(f"- {event_type} in {repo}")