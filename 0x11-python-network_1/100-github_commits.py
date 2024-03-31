#!/usr/bin/python3
"""The Holberton School staff evaluates candidates applying for a back-end position with multiple technical challenges, like this one:

Please list 10 commits (from the most recent to oldest) of the repository “rails” by the user “rails”
You must use the GitHub API, here is the documentation https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
"""

import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[2], sys.argv[1])
    r = request.get(url)
    commits = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha")
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
