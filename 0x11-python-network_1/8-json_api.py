#!/usr/bin/python3
'''search with parameter'''

if __name__ == "__main__":
    import requests
    import sys
    q = "" if len(sys.argv) == 1 else sys.argv[1]
    params = {'q': q}
    r = requests.post('http://0.0.0.0:5000/search_user', data=params)
    try:
        result = r.json()
        if not result:
            print("No result")
        else:
            print(f"[{result['id']}] {result['name']}")
    except ValueError:
        print("Not a valid JSON")
