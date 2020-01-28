#!/usr/bin/env python3
import re
import sys

def get_url(fname,patt):
    cpatt = re.compile(patt)
    results = []
    with open(fname,'rb') as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                results.append(m)
    return results

if __name__ == '__main__':
    patt = r'^http|https://[.\w-]+\.(png|jpg|jpeg|gif)$'
    print(get_url(sys.argv[1],patt))