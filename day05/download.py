#!/usr/bin/env python3

import os
import re
import wget
from urllib import error

def get_url(fname,patt,encoding=None):
    url_list = []
    cpatt = re.compile(patt)
    with open(fname,encoding=encoding) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                url_list.append(m.group())
        return url_list

if __name__ == '__main__':
    img_dir = '/tmp/163'
    url163 = 'http://www.163.com'
    fname163 = '/tmp/163/163.html'

    if not os.path.exists(img_dir):
        os.mkdir(img_dir)
    if not os.path.exists(fname163):
        wget.download(url163,fname163)

    img_patt = '(http|https)://[\w.-/]+\.(gif|png|jpg|jpeg)'
    img_list = get_url(fname163,img_patt,'gbk')

    for url in img_list:
        try:
            wget.download(url,img_dir)
        except error.HTTPError:
            pass
