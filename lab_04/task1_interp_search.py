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

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, node, data):
        if node is None:
            return Node(data)

        if data < node.data:
            node.left = self._insert(node.left, data)
        else:
            node.right = self._insert(node.right, data)

        return node

    def interpolation_search(self, data):
        return self._interpolation_search(self.root, data, self._min_value(), self._max_value())


    def _interpolation_search(self, node, data, min_val, max_val):
        if node is None or min_val > max_val:
            return False

        if node.data == data:
            return True

        if min_val == max_val:
            return False

        mid = min_val + ((max_val - min_val) // (self._max_value() - self._min_value())) * (data - self._min_value())

        if node.data < mid:
            return self._interpolation_search(node.right, data, node.data + 1, max_val)
        else:
            return self._interpolation_search(node.left, data, min_val, node.data - 1)

    def _min_value(self):
        node = self.root
        while node.left:
            node = node.left
        return node.data

    def _max_value(self):
        node = self.root
        while node.right:
            node = node.right
        return node.data

    def print_tree_elements(self):
        elements = []
        self._inorder_traversal(self.root, elements)
        print("Элементы дерева:", elements)

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
result = tree.interpolation_search(target)
end_time = time.time()
search_time = end_time - start_time
print(f"Поиск в дереве: {result}, время работы: {search_time:.6f} секунд")