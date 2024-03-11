from struct import *

with open('bracket.txt', 'r', encoding='utf-8') as f:
    text = f.readline().strip('\n')
print(text)

flag = 1
stack = Stack()
for i in text:
    if i == '(':
        stack.push_stack(i)
    elif i == ')' and len(stack) != 0:
        stack.pop_stack()
    else:
        flag = 0
        break

if len(stack) == 0 and flag:
    print('Баланс скобок сохранен')
else:
    print('Баланс скобок не сохранен')


