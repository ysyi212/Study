#!/root/ysy/python/bin/python3
'''account
keep accounts
'''
import time
import os
import pickle

def save_fun(fname):
    try:
        amount = int(input('sum of money: '))
        comment = input('comment: ')
    except ValueError:
        print('invalid input')
        return
    except (EOFError,KeyboardInterrupt):
        return

    date = time.strftime('%Y-%m-%d')
    with open(fname,'rb') as fobj:
        records = pickle.load(fobj)
    balance = records[-1][-2] + amount

    record = [date,amount,0,balance,comment]
    records.append(record)
    with open(fname,'wb') as fobj:
        pickle.dump(records,fobj)

def cost_fun(fname):
    try:
        amount = int(input('sum of money: '))
        comment = input('comment: ')
    except ValueError:
        print('invalid input')
        return
    except (EOFError,KeyboardInterrupt):
        return

    date = time.strftime('%Y-%m-%d')
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)
    balance = records[-1][-2] - amount

    record = [date,0,amount,balance,comment]
    records.append(record)
    with open(fname, 'wb') as fobj:
        pickle.dump(records, fobj)

def show_fun(fname):
    with open(fname,'rb') as fobj:
        records = pickle.load(fobj)

    print('%-16s%-8s%-8s%-10s%-20s' % ('date','save','cost','balance','comment'))
    for record in records:
        print('%-16s%-8s%-8s%-10s%-20s' % tuple(record))

def menu_fun():
    info = '''(0)save
(1)cost
(2)show
(3)quit
make your choice(0/1/2/3): '''

    fname = 'account.data'
    init = [['2020-01-10',0,0,10000,'init']]

    if not os.path.exists(fname):
        with open(fname,'wb') as fobj:
            pickle._dump(init,fobj)

    mon = {'0':save_fun,'1':cost_fun,'2':show_fun}

    while 1:
        try:
            choice = input(info).strip()
        except (EOFError, KeyboardInterrupt,KeyError):
            print('\nByebye~')
            break
        if choice not in '0123':
            print("the choice must in '0/1/2/3'")
            continue
        elif choice == '3':
            print('\nByebye~')
            break
        else:
            mon[choice](fname)

if __name__ == '__main__':
    menu_fun()