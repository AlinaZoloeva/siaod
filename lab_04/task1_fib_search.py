import time

from task1_bin_tree import *

# Поиск элемента
tree.print_tree_elements()
target = int(input("Введите элемент для поиска: "))
start_time = time.time()
result = tree.fibonacci_search(target)
end_time = time.time()
search_time = end_time - start_time
print(f"Поиск в дереве: {result}, время работы: {search_time:.6f} секунд")