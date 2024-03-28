#!/usr/bin/python3
'''sends POST request to an URL with email parameter'''

if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys

    data = urllib.parse.urlencode({'email': sys.argv[2]})
    data = data.encode("ascii")
    url = sys.argv[1]
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        result = response.read().decode("utf-8")
    print(result)
