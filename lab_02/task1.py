from struct import *

with open('books.txt', 'r', encoding='utf-8') as f:
    books1 = Deque()
    for book in f:
        books1.append_dq(book.strip('\n'))

    books2 = Deque()

    while not books1.is_empty_deque():
        el = books1.pop_dq()
        while not books2.is_empty_deque() and books2.peek() < el:
            books1.appendleft_dq(books2.pop_dq())
        books2.append_dq(el)

    while not books2.is_empty_deque():
        print(books2.pop_dq())




