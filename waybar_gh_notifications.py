#!/usr/bin/env python3
"""
Waybar script to display GitHub notifications.
Usage: waybar_github_notifications.py <github_token>
"""

import sys
import json
from github import Github, GithubException, Auth

FORMAT = " {}"
COLOR_GOOD = "#00ff00"  # green
COLOR_BAD = "#ff0000"   # red

def get_notifications(token):
    try:
        g = Github(auth=Auth.Token(token))
        user = g.get_user()
        notifications = user.get_notifications()
        count = notifications.totalCount if hasattr(notifications, "totalCount") else len(list(notifications))
        return count
    except GithubException as e:
        print(json.dumps({"text": " ?", "tooltip": str(e), "color": COLOR_BAD}))
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print(json.dumps({"text": " ?", "tooltip": "Missing token", "color": COLOR_BAD}))
        sys.exit(1)
    token = sys.argv[1]
    count = get_notifications(token)
    color = COLOR_BAD if count > 0 else COLOR_GOOD
    print(json.dumps({
        "text": FORMAT.format(count),
        "tooltip": f"{count} GitHub notifications",
        "color": color
    }))

if __name__ == "__main__":
    main()
