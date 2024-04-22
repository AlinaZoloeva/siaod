import random
import time


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._add(data, self.root)

    def _add(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._add(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._add(data, node.right)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data < node.data:
            if node.left:
                self._insert(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right:
                self._insert(data, node.right)
            else:
                node.right = Node(data)

    def search(self, data):
        return self._search(data, self.root)

    def _search(self, data, node):
        if node is None:
            return False
        if node.data == data:
            return True
        elif data < node.data:
            return self._search(data, node.left)
        else:
            return self._search(data, node.right)

    def remove(self, data):
        self.root = self._remove(data, self.root)

    def _remove(self, data, node):
        if node is None:
            return node
        if data < node.data:
            node.left = self._remove(data, node.left)
        elif data > node.data:
            node.right = self._remove(data, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = self._find_min(node.right)
                node.data = successor.data
                node.right = self._remove(successor.data, node.right)
        return node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

    def print_tree_elements(self):
        elements = []
        self._inorder_traversal(self.root, elements)
        print("Элементы дерева:", elements)

    # Фибоначчиев поиск
    def fibonacci_search(self, data):
        elements = []
        self._inorder_traversal(self.root, elements)
        return self._fibonacci_search(data, elements)

    def _fibonacci_search(self, data, elements):
        n = len(elements)
        fib_m2 = 0  # (m-2)-е число Фибоначчи
        fib_m1 = 1  # (m-1)-е число Фибоначчи
        fib_m = fib_m2 + fib_m1  # m-е число Фибоначчи

        while fib_m < n:
            fib_m2 = fib_m1
            fib_m1 = fib_m
            fib_m = fib_m2 + fib_m1

        offset = -1

        while fib_m > 1:
            i = min(offset + fib_m2, n - 1)

            if elements[i] < data:
                fib_m = fib_m1
                fib_m1 = fib_m2
                fib_m2 = fib_m - fib_m1
                offset = i

            elif elements[i] > data:
                fib_m = fib_m2
                fib_m1 = fib_m1 - fib_m2
                fib_m2 = fib_m - fib_m1

            else:
                return i

        if fib_m1 and offset < n - 1 and elements[offset + 1] == data:
            return offset + 1

        return -1

    def _inorder_traversal(self, node, elements):
        if node:
            self._inorder_traversal(node.left, elements)
            elements.append(node.data)
            self._inorder_traversal(node.right, elements)


# Генерация начального набора случайных данных
start = int(input("Введите минимальное значение генерируемых объектов: "))
end = int(input("Введите максимальное значение генерируемых объектов: "))
data = [random.randint(start, end) for _ in range(end)]
data.sort()

# Создание бинарного дерева
tree = BinaryTree()
start_time = time.time()
for item in data:
    tree.insert(item)
end_time = time.time()
tree_creation_time = end_time - start_time
print(f"Время создания дерева: {tree_creation_time:.6f} секунд")
tree.print_tree_elements()

# Поиск элемента
target = int(input("Введите элемент для поиска: "))
start_time = time.time()
result = tree.search(target)
end_time = time.time()
search_time = end_time - start_time
print(f"Поиск в дереве: {result}, время работы: {search_time:.6f} секунд")

# Добавление элемента
new_element = int(input("Введите элемент который хотите добавить: "))
tree.add(new_element)
print("Элементы дерева:")
tree.print_tree_elements()

# Удаление элемента
delete = int(input("Введите элемент который хотите удалить: "))
start_time = time.time()
tree.remove(delete)
end_time = time.time()
removal_time = end_time - start_time
print(f"Удаление из дерева: время работы: {removal_time:.6f} секунд")
print("После удаления:")
tree.print_tree_elements()