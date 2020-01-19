#!/root/ysy/python/bin/python3
'''cp

copy file
'''

a = open('/bin/ls','rb')
b = open('/root/ls','wb')
data = a.read()
b.write(data)
a.close()
b.close()