import random
from struct import *

alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
random.shuffle(alphabet)
alphabet = ''.join(alphabet)

code = Deque(alphabet)

def encode(char):
    for i in range(len(code)):
        x = code.popleft_dq()
        
        if x == char:
            code.append_dq(x)
            val = code.popleft_dq()
            code.append_dq(val)

            return val
        code.append_dq(x)

def decode(char):
    for i in range(len(code)):
        x = code.pop_dq()

        if x == char:
            code.appendleft_dq(x)
            val = code.pop_dq()
            code.appendleft_dq(val)

            return val
        code.appendleft_dq(x)


with open('text.txt', 'r', encoding='utf-8') as f:
    message = f.readline().strip('\n').lower()

encoded = ''

for letter in message:
    if encoded_letter := encode(letter):
        encoded += encoded_letter
    else:
        encoded += letter

print(encoded)


decoded = ''

for letter in encoded:
    if decoded_letter := decode(letter):
        decoded += decoded_letter
    else:
        decoded += letter

print(decoded)



