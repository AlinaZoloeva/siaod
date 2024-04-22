import itertools

s = 'asdf'
s = list(s)
s.insert(1, list('abf'))
print(s)
print(list(itertools.chain(*s)))

