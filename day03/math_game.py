#!/root/ysy/python/bin/python3
'''math_game
'''
from random import randint, choice

def exam():
    nums = [randint(1,100)for i in range(2)]
    nums.sort(reverse=True)
    op = choice('+-')

    if op == '+':
        result = nums[0] + nums[1]
    else:
        result = nums[0] - nums[1]

    info = '%s %s %s = '%(nums[0],op,nums[1])
    times = 0

    while times < 3:
        try:
            answer = input(info)
        except (EOFError,KeyboardInterrupt):
            print('\ninvalid input')
            return
        if answer == result:
            print('Correct!')
            break
        else:
            print('Wrong...')
            times += 1
            continue

def main():
    while 1:
        exam()
        try:
            yn = input('continue(y/n)?').strip()[0]
        except IndexError:
            continue
        except (EOFError,KeyboardInterrupt):
            yn = 'n'

        if yn in 'nN':
            print('\nByebye~')
            break

if __name__ == '__main__':
    main()