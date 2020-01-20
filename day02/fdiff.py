#!/root/ysy/python/bin/python3
'''fdiff
compare two files
'''
import sys

def fdiff():
    with open(sys.argv[1]) as f1:
        aset = set(f1)
    with open(sys.argv[2]) as f2:
        bset = set(f2)
    with open(sys.argv[3],'w') as f3:
        f3.writelines(bset-aset)

if __name__ == '__main__':
    fdiff()