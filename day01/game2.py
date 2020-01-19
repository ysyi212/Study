#!/root/ysy/python/bin/python3
'''game2
best of three
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
player_count = 0
computer_count = 0

while player_count < 2 and computer_count < 2:
    computer = random.choice(all_choices)
    index = int(input(prompt))
    player = all_choices[index]
    print('your choice:%s,computer choice:%s' %(player,computer))
    if [player,computer] in win_list:
        player_count += 1
        print('\033[32;1mYou win!\033[0m')
    elif player == computer:
        print('\033[33;1mDraw\033[0m')
    else:
        computer_count += 1
        print('\033[31;1mYou lose...\033[0m')
if player_count > computer_count:
    print('\033[46;3mThe final winner is you!\033[0m')
else:
    print('\033[45;5mSorry,you lose...\033[0m')