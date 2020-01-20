#!/root/ysy/python/bin/python3
'''login-new
register and login
'''
import getpass

ulist = {}

def reg_fun():
    username = input('username: ')
    if username in ulist:
        print('%s is existed'% username)
    else:
        password = input('password: ')
        ulist[username] = password

def login_fun():
    username = input('username: ')
    password = getpass.getpass('password: ')
    if ulist.get(username) != password:
        print('Login fail...')
    else:
        print('Login in!')

def show_menu():
    info = '''(0)register
(1)login
(2)quit
Please input your choice(0/1/2): '''

    while 1:
        choice = input(info).strip()
        if choice not in '012':
            print('\033[31;1mInvalid input\033[0m\n')
            continue
        elif choice == '2':
            print('Byebye~\n')
            break
        elif choice == '0':
            reg_fun()
            continue
        else:
            login_fun()
            break

if __name__ == '__main__':
    show_menu()