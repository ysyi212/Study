#!/root/ysy/python/bin/python3
'''mydiv
judge mydiv
'''
try:
    div = int(input('input a divisor: '))
    num = 100 / div
except (KeyboardInterrupt,EOFError):
    print()
    exit()
except ZeroDivisionError:
    print("you shouldn't input zero")
    exit()
except ValueError:
    print("you should input a number")
    exit()
else:
    print("100 / %s = %s"% (div,num))
finally:
    print("Done")
