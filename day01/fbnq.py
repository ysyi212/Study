#!/root/ysy/python/bin/python3
'''fbnq

Fibonacci sequence
'''
num = int(input('enter sequence length: '))
seq = [0,1]

for i in range(num-len(seq)):
    seq.append(seq[-2] + seq[-1])
print(seq)