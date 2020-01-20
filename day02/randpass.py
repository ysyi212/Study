#!/root/ysy/python/bin/python3
'''randpass

generate random password
'''

from random import choice
from string import ascii_letters,digits

def randpass(n=8):

    all_chs = ascii_letters + digits
    result = ''

    for i in range(0,n):
        ch = choice(all_chs)
        result += ch

    return result

if __name__ == '__main__':
    print(randpass())