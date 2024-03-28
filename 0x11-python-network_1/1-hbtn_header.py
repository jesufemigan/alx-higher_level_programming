#!/usr/bin/python3
'''a module that displays value of X-Request-Id'''

if __name__ == '__main__':
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        pass
    print(response.getheader("X-Request-Id"))
