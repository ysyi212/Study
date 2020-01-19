#!/root/ysy/python/bin/python3
'''mtable

Multiplication table
'''
for i in range(0,10):
    for j in range(0,i+1):
        j += 1
        print('%sX%s=%s  ' %(j,i,i*j),end='')
    print()