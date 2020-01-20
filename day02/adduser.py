#!/root/ysy/python/bin/python3
'''adduser
create user and password
write in a file
'''

import sys
import randpass
import subprocess

def add_user(username,password,fname):
    info = '''
    username:%s
    password:%s
    '''
    subprocess.run('useradd %s'%username,shell=True)
    subprocess.run('echo %s | passwd --stdin %s'%(password,username),shell=True)
    with open(fname,'a') as fobj:
        fobj.write(info %(username,password))

if __name__ == '__main__':
    username = sys.argv[1]
    password = randpass.randpass()
    fname = sys.argv[2]
    add_user(username,password,fname)
