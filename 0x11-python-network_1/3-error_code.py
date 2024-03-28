#!/usr/bin/python3
'''sends request and shows error code'''

if __name__ == "__main__":
    import urllib.request
    from urllib.error import URLError
    import sys
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            content = response.read()
            print(content.decode("utf-8"))
    except URLError as e:
        if hasattr(e, 'code'):
            print("Error code:", e.code)
