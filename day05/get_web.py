#!/usr/bin/env python3

from urllib.request import urlopen
import sys

def get_web(url,fname):
    html = urlopen(url)
    with open(fname,'wb') as fobj:
        while 1:
            data = html.read(4096)
            if not data:
                break
            fobj.write(data)
    html.close()

if __name__ == '__main__':
    get_web(sys.argv[1],sys.argv[2])