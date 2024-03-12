import json

import requests


def get_date(datetime: str) -> str:
    year = datetime[:4]
    month = datetime[5:7]
    day = datetime[8:10]
    time = datetime[11:16]

    return day + "/" + month + "/" + year + " " + time


def read_last_10_commits(repo: str) -> None:
    url = f"https://api.github.com/repos/mouredev/{repo}/commits"
    headers = {"Accept": "application/json", "Content-Type": "application/json"}

    page = requests.get(url, headers)
    commits = json.loads(page.text)

    for i in range(0, 10):
        _hash = commits[i]["sha"]
        author = commits[i]["commit"]["author"]["name"]
        message = commits[i]["commit"]["message"]
        datetime = get_date(commits[i]["commit"]["author"]["date"])

        print(f"Commit {i + 1} | {_hash} | {author} | {message} | {datetime}")


read_last_10_commits("retos-programacion-2023")
