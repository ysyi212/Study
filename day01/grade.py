#!/root/ysy/python/bin/python3
#coding:utf8

'''grade
judge score
'''

score = int(input('input your score: '))

if score >= 90:
    print('excellent')
elif score >= 80:
    print('good')
elif score >= 70:
    print('fine')
elif score >= 60:
    print('qualified')
else:
    print('\033[31;1myou must work hard!\033[0m')