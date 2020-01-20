#!/root/ysy/python/bin/python3
'''stack
you can stack in,out and show
'''

stack = []

def stack_put():
    text = input('input some text: \n')
    stack.append(text)

def stack_out():
    if stack:
        print('kick %s \n'% stack.pop())
    else:
        print('stack is empty \n')

def stack_show():
    print('%s \n'% stack)

def show_menu():
    info = '''(0) stack_put
(1) stack_out
(2) stack_show
(3) quit
Please input your choice(0/1/2/3): '''

    while 1:
        choice = input(info).strip()
        if choice not in '0123':
            print('\033[31;1mInvalid input\033[0m\n')
            continue
        elif choice == '3':
            print('Byebye~\n')
            break
        elif choice == '0':
            stack_put()
        elif choice == '1':
            stack_out()
        else:
            stack_show()

if __name__ == '__main__':
    show_menu()