#!/usr/bin/python3
'''A module that fetches froma url'''

if __name__ == '__main__':
    import urllib.request
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        content = response.read()
        content_type = content.__class__
        utf8 = content.decode("utf-8")

    print(f'Body response:\n\t- type: {content_type}\n\t- content: \
    {content}\n\t- utf8 content: {utf8}')
