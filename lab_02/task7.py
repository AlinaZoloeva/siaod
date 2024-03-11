from struct import *

with open('task7.txt', 'r', encoding='utf-8') as f:
    digits = f.readline().strip('\n')

digits = digits.split(' ')

pos = Deque()
neg = Deque()

for i in digits:
    if i.find('-') != -1:
        neg.append_dq(i)
    else:
        pos.append_dq(i)

print(' '.join(neg.deque) + ' ' +  ' '.join(pos.deque))