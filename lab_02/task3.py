import random

n = int(input('кол-во дисков: '))
min_disk = int(input('мин значение рамзера диска: '))
max_disk = int(input('макс значение размера диска: '))


def move_disk(kernel, source, destination):
    disk = kernel[source].pop()
    kernel[destination].append(disk)
    print(f"Move disk {disk} from {source} to {destination}")


def hanoi_recursive(n, kernel, source, auxiliary, destination):
    if n > 0:
        hanoi_recursive(n-1, kernel, source, destination, auxiliary)
        move_disk(kernel, source, destination)
        hanoi_recursive(n-1, kernel, auxiliary, source, destination)


def solve_hanoi():
    hanoi_recursive(n, kernel, 'A', 'B', 'C')


kernel = {'A': [], 'B': [], 'C': []}
for i in range(n):
    kernel['A'].append(random.randint(min_disk, max_disk))
    kernel['A'].sort(reverse=True)
print(kernel['A'])

solve_hanoi()