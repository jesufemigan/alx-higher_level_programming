#!/usr/bin/python3
'''post request using requests library'''

if __name__ == "__main__":
    import requests
    import sys
    r = requests.post(sys.argv[1], {'email': sys.argv[2]})
    print(r.text)
