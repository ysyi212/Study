#!/root/ysy/python/bin/python3
'''game

Rock-paper-scissors
'''

import random

all_choices = ['Rock','Paper','Scissors']
win_list = [['Rock','Scissors'],['Scissors','Paper'],['Paper','Rock']]
prompt = '''
0/Rock,
1/Paper,
2/Scissors
Please decide:
'''
computer = random.choice(all_choices)
index = int(input(prompt))
player = all_choices[index]

print('player:'+player,'computer:'+computer)
if [player,computer] in win_list:
    print('\033[32;1mYou win!\033[0m')
elif player == computer:
    print('\033[33;1mDraw\033[0m')
else:
    print('\033[31;1mYou lose...\033[0m')

# player = int(input('Please decide (0/Rock,1/Paper,2/Scissors): '))
# computer = random.choice([0,1,2])
#
# print('palyer:' + str(player))
# print('computer:' + str(computer))
# if player > computer:
#     print('You win!')
# elif player == computer:
#     print('Draw')
# else:
#     print('You lose...')