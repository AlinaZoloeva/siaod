'''
import collections

class Stack:
    def __init__(self):
        self.stack = []

    def __len__(self):
        return len(self.stack)

    def is_empty_stack(self):
        return not(bool(len(self.stack)))

    def push_stack(self, elem):
        self.stack.insert(0, elem)

    def pop_stack(self):
        return self.stack.pop(0)

class Deque:
    def __init__(self, *args, **kwargs):
        if len(args) == 0:
            self.deque = collections.deque()
        else:
            self.deque = collections.deque(args[0])

    def __len__(self):
        return len(self.deque)

    def is_empty_deque(self):
        return not(bool(len(self.deque)))

    def appendleft_dq(self, elem):
        self.deque.appendleft(elem)

    def append_dq(self, elem):
        self.deque.append(elem)

    def popleft_dq(self):
        return self.deque.popleft()

    def pop_dq(self):
        return self.deque.pop()

    def peek(self):
        return self.deque[-1]
'''
import itertools
import re

a = input()
b = input()

b_arr = re.split('<', b)


s = list(b_arr[0])


curr_pos = len(s) - 1
for i in range(1, len(b_arr)):
    if '>' in b_arr[i]:
        if b_arr[i][:b_arr[i].find('>')] == 'left':
            if curr_pos != 0:
                curr_pos -= 1

        elif b_arr[i][:b_arr[i].find('>')] == 'bspace':
            if len(s) != 0:
                s.pop(curr_pos)
                curr_pos -= 1
        elif b_arr[i][:b_arr[i].find('>')] == 'delete':
            if curr_pos != len(s) - 1 and len(s) != 0:
                s.pop(curr_pos + 1)

        elif b_arr[i][:b_arr[i].find('>')] == 'right':
            if curr_pos != len(s):
                curr_pos += 1

        if b_arr[i].find('>') != len(b_arr[i]) - 1:
            s.insert(curr_pos + 1, b_arr[i][b_arr[i].find('>') + 1:])
            curr_pos += len(b_arr[i][b_arr[i].find('>') + 1:])
            s = list(itertools.chain(*s))

if ''.join(s) == a:
    print('Yes')
else:
    print('No')






