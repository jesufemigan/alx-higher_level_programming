#!/usr/bin/python3
'''use Github API'''

if __name__ == "__main__":
    import requests
    import sys
    url = "https://api.github.com/users/" + sys.argv[1]
    # token = "github_pat_11ALOLOSA0kivU4eXnI1jQ_CfzP7IDwqDtj5P2mT7\
# tpbWZYl7CZbd9TV9K35J4NSqXPH3ZQVIDM7qaeADP"
    headers = {"Accept": "application/vnd.github+json",
               "Authorization": sys.argv[2],
               "X-Github-Api-Version": "2022-11-28"}
    r = requests.get(url, headers=headers)
    user = r.json()
    print(user.get('id'))
