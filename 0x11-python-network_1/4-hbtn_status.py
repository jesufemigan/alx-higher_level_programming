#!/usr/bin/python3
'''fetch using requests'''

if __name__ == "__main__":
    import requests
    url = "https://alx-intranet.hbtn.io/status"
    r = requests.get(url)
    result = [r.text.__class__, r.text]
    print("Body response")
    for i in result:
        print(f"\t- type: {i}")
