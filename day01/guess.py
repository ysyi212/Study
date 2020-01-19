#!/root/ysy/python/bin/python3
'''guess
guess which is the right number in 100
'''

import random

prompt = '''
choose the number between 0~100:
'''
sys_num = random.randint(0,100)
times = 0

while times < 5:
    your_num = int(input(prompt))
    if your_num > sys_num:
        print('Your number is larger~')
    elif your_num < sys_num:
        print('Your number is smaller~')
    else:
        print('\033[32;1mYou guess it!\033[0m')
        break
    times += 1
else:
    print('\033[31;1mThe true number is %s\033[0m' %sys_num)