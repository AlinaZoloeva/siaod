from struct import *

with open('task6.txt', 'r', encoding='utf=8') as f:
    string = f.readline().strip('\n')

digits = Stack()
letters = Stack()
other = Stack()

for i in string:
    if i.isdigit():
        digits.push_stack(i)
    elif i.isalpha():
        letters.push_stack(i)
    else:
        other.push_stack(i)

print(''.join(digits.stack)[::-1] + ''.join(letters.stack)[::-1] + ''.join(other.stack)[::-1])