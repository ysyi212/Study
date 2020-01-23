#!/root/ysy/python/bin/python3
'''count_patt
analysis apache accesslog
'''
import re

def count_patt(fname,patt):
    patt_dict = {}
    cpatt = re.compile(patt)

    with open(fname) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                key = m.group()
                patt_dict[key] = patt_dict.get(key,0) + 1
    return patt_dict

if __name__ == '__main__':
    fname = '/var/log/httpd/access_log'
    ip = '^(\d+\.){3}\d+'
    br = 'Firefox|MSIE|Chrome'
    result1 = count_patt(fname,ip)
    result2 = count_patt(fname,br)
    print(result1)
    print(result2)
    result3 = list(result1.items())
    result3.sort(key = lambda seq:seq[-1],reverse=True)
    print(result3)