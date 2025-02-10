from collections import defaultdict


def update(array, index, value):
    length = len(array)
    while index < length:
        array[index] += value
        index += index & -index


def get_total(array, index):
    total = 0
    while index:
        total += array[index]
        index -= index & -index
    return total


n = int(input())
items = {}
counter = {}
m = 0
for _ in range(n):
    x, k = input().strip().split()
    k = int(k)
    items[x] = k
    m = max(m, k)

counter = defaultdict(int)
tree = [0] * (m + 1)
size = 0
q = int(input())
for _ in range(q):
    symbol, x = input().strip().split()
    if symbol == '+':
        k = items[x]
        counter[x] += 1
        size += 1
        update(tree, k, 1)
    elif symbol == '-':
        k = items[x]
        if counter[x] > 0:
            counter[x] -= 1
            size -= 1
            update(tree, k, -1)
    elif symbol == '?':
        y = int(x)
        print(size - get_total(tree, y))
