import random

# Простое рехэширование
class HashTable1:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash(key)
        self.table[index].append((key, value))

    def search(self, key):
        index = self.hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def rehash(self, new_size):
        old_table = self.table
        self.size = new_size
        self.table = [[] for _ in range(new_size)]

        for bucket in old_table:
            for key, value in bucket:
                self.insert(key, value)

# рехэширование с помощью псевдослучайных чисел
class HashTable2:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.rehash_count = 0

    def hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash(key)
        self.table[index].append((key, value))

        # Триггер для рехэширования
        if len(self.table[index]) > self.size // 2:
            self.rehash(self.size * 2)

    def search(self, key):
        index = self.hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def rehash(self, new_size):
        old_table = self.table
        self.size = new_size
        self.table = [[] for _ in range(new_size)]
        self.rehash_count += 1

        for bucket in old_table:
            for key, value in bucket:
                self.insert(key, value)

        # Перемешивание таблицы после рехэширования
        random.shuffle(self.table)


# метод цепочек
class HashTable3:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash(key)
        for k, v in self.table[index]:
            if k == key:
                self.table[index].remove((k, v))
                break
        self.table[index].append((key, value))

    def search(self, key):
        index = self.hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self.hash(key)
        for k, v in self.table[index]:
            if k == key:
                self.table[index].remove((k, v))
                return v
        return None

# Простое рехэширование
ht = HashTable1(3)
ht.insert("alina", 10)
ht.insert("sveta", 20)
ht.insert("kamila", 30)
ht.rehash(6)
print(ht.search("alina"))  # 10

# Рехэширование с помощью псевдослучайных чисел
ht = HashTable2(3)
ht.insert("alina", 10)
ht.insert("sveta", 20)
ht.insert("kamila", 30)
ht.insert("dog", 40)  # Триггер для рехэширования
print(ht.search("alina"))  # 10

# Метод цепочек
ht = HashTable3(3)
ht.insert("alina", 10)
ht.insert("sveta", 20)
ht.insert("kamila", 30)
ht.insert("alina", 40)  # Обновление значения для ключа "apple"
print(ht.search("alina"))  # 40
ht.delete("sveta")
print(ht.search("sveta"))  # None
