#!/root/ysy/python/bin/python3
'''formatoutput
'''
import os

contents = []
print('input some lines,finish with "end".')
while 1:
    line = input('> ')
    if line == 'end':
        break
    contents.append(line)
print("+%s+"% ('*' * 48))
for line in contents:
    print("+%s+" % line.center(48))
print("+%s+"% ('*' * 48))