from struct import *

with open('bracket_sq.txt', 'r', encoding='utf-8') as f:
    string = f.readline().strip('\n')

deque = Deque()

flag = 1
for i in string:
    if i == '[':
        deque.append_dq(i)
    elif i == ']' and len(deque) != 0:
        deque.pop_dq()
    else:
        flag = 0

if len(deque) == 0 and flag:
    print('Баланс скобок сохранен')
else:
    print('Баланс скобок не сохранен')



