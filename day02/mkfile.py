#!/root/ysy/python/bin/python3
'''mkfile
make file and write something in it
'''
import os

def get_fname():
    while 1:
        fname = input('input your filename: ')
        if not os.path.exists(fname):
            break
        print('%s is exist.'% fname)
    return fname

def get_contents():
    contents = []
    print('input your contents,finish with "end".')
    while 1:
        line = input('> ')
        if line == 'end':
            break
        contents.append(line)
    return contents

def wfile (fname,contents):
    with open(fname,'w') as fobj:
        fobj.writelines(contents)

if __name__ == '__main__':
    fname = get_fname()
    contents = get_contents()
    contents = ['%s\n'% line for line in contents]
    wfile(fname,contents)

