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
