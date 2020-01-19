#!/root/ysy/python/bin/python3
'''login2
judge username and password
'''
import getpass

name = input('input yourname:')
password = getpass.getpass('input password:')

if name == 'bob' and password == '123456':
    print('\033[32;1mlogin successful\033[0m')
else:
    print('\033[31;1mlogin incorrect\033[0m')