import random
import time

# random.uniform(a, b) - если вдруг нужна генерация вещественных чисел

user_n = input('row count: ')
user_m = input('column count: ')

user_min_limit = input('Input min value: ')
user_max_limit = input('Input max value: ')


if not (isinstance(int(user_m), int) and isinstance(int(user_n), int) and
        isinstance(int(user_min_limit), int) and isinstance(int(user_max_limit), int)):
    print('Error value')
    exit()

try:
    mtrx = [[random.randrange(int(user_min_limit), int(user_max_limit)) for j in range(int(user_m))] for i in range(int(user_n))]
except:
    print('min_value and max_value are the same')
    exit()

for i in range(int(user_n)):
    for j in range(int(user_m)):
        print(mtrx[i][j], end=' ')
    print()


