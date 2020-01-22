#!/root/ysy/python/bin/python3
'''os_module
know os
'''

import os
import pprint

os.chdir('/tmp')
os.getcwd()
os.mkdir('example')
os.chdir('/tmp/example')
os.getcwd()
os.mknod('test.txt')
with open('/tmp/example/test.txt','w') as fobj:
    fobj.write('foo bar')

os.path.abspath('test.txt')
os.path.basename('/tmp/example/test.txt')
os.path.dirname('/tmp/example/test.txt')
os.path.split('/tmp/example/test.txt')
os.path.join('/tmp/example','test.txt')
os.path.isabs('example/test.txt')
os.path.isfile('/tmp/example/test.txt')
os.path.isdir('/tmp')
os.path.islink('/etc/host')
os.path.ismount('/boot')
os.path.exists('/home')

os.listdir('/tmp/example')

os.remove('test.txt')
os.removedirs('/tmp/example')

# result = list(os.walk('/etc/security'))
# pprint.pprint(result)
# print()
#
# for path,folders,files in os.walk('/etc/security'):
#     print('%s\n%s\n%s'%(path,folders,files))
#     print()

for path,folders,files in os.walk('/etc/security'):
    print('%s:'% path)
    for d in folders:
        print(d,end ='\t')
    for f in files:
        print(f,end ='\t')
    print('\n')