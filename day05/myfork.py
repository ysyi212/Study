#!/usr/bin/env python3
import os
import time
import datetime

pid = os.fork()
if not pid:
    print('In parent')
    time.sleep(10)
    print('parent exit')
else:
    for i in range(5):
        print(datetime.datetime.now())
        time.sleep(1)
    print('child exit')