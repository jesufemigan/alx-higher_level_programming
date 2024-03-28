#!/usr/bin/python3
'''interview with githubAPI'''

if __name__ == "__main__":
    import requests
    import sys
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    token = "github_pat_11ALOLOSA0kivU4eXnI1jQ_CfzP7IDwqDtj5P2mT7tpbWZ\
Yl7CZbd9TV9K35J4NSqXPH3ZQVIDM7qaeADP"
    headers = {"Accept": "application/vnd.github+json",
               "Authorization": f"Bearer {token}",
               "X-Github-Api-Version": "2022-11-28"}
    params = {"per_page": 10}
    r = requests.get(url, headers=headers, params=params)
    response = r.json()

    for commit in response:
        print(f"{commit['commit']['tree']['sha']}:\
 {commit['commit']['author']['name']}")
