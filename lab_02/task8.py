from struct import Stack

lines = Stack()

with open('task8_1.txt', 'r', encoding='utf-8') as f:
    for i in f.readlines():
        lines.push_stack(i)

lines.stack[0] += '\n'
lines.stack[-1] = lines.stack[-1].replace('\n', '')

with open('task8_2.txt', 'w', encoding='utf-8') as f:
    for i in range(len(lines)):
        f.write(lines.pop_stack())

